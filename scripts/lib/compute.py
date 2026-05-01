# -*- coding: utf-8 -*-
"""Python port of the HTML computeScenario() engine.

Kept in sync with index.html's computeScenario() and model.html's ModelView.
If you change the math in the HTML files, mirror it here and run the snapshot
script to regenerate the baseline.
"""
from __future__ import annotations

SCENARIO_ORDER = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]


def som_of(market):
    """SOM in $M = sum over regions of (patientsK * reachPct%*wtpPct%*priceK)."""
    if not market or "company_slice" not in market or "regions" not in market:
        return 0.0
    total = 0.0
    for rk, cs in market["company_slice"].items():
        tr = market["regions"].get(rk)
        if not tr or not cs:
            continue
        total += (tr.get("patientsK", 0) or 0) * (cs.get("reachPct", 0) / 100) \
                 * (cs.get("wtpPct", 0) / 100) * (cs.get("priceK", 0) or 0)
    return total


def tam_of(market):
    """TAM in $M = sum over regions of (patientsK * wtpPct% * priceK)."""
    if not market or "regions" not in market:
        return 0.0
    total = 0.0
    for r in market["regions"].values():
        if not r:
            continue
        total += (r.get("patientsK", 0) or 0) * (r.get("wtpPct", 0) / 100) \
                 * (r.get("priceK", 0) or 0)
    return total


def _is_commercial(asset):
    stg = (asset.get("stage", "") or "").lower()
    return asset.get("id") == "commercial" or "commercial" in stg \
        or "launched" in stg or "marketed" in stg


def compute_tp(cfg, scenario_key):
    """Compute target price for one scenario. Mirrors computeScenario() in
    index.html and model.html. Returns None if scenario missing OR if the
    company is private (no equity tradeable -- TP would be meaningless)."""
    scen = cfg.get("scenarios", {}).get(scenario_key)
    if not scen:
        return None
    co = cfg["company"]
    if co.get("private"):
        return None
    val = scen.get("val", {})
    is_sotp = val.get("pipelineDR") is not None

    pipe_ra = 0.0
    total_ra = 0.0
    total_gross = 0.0

    for asset in cfg["assets"]:
        is_comm = _is_commercial(asset)
        for ind in asset["indications"]:
            asmp = scen.get("assumptions", {}).get(asset["id"], {}).get(
                ind["id"], {"pos": 0, "apr": 0, "pen": 1})
            m = ind.get("market", {}) or {}
            # SOTP: commercial assets excluded (they feed into commercialRevM directly)
            if is_comm and is_sotp:
                continue
            pk = 0.0
            if "company_slice" in m and "regions" in m:
                pk = som_of(m)
                if m.get("cagrPct"):
                    yr = (m.get("peakYear", 2033) - 2026)
                    pk *= (1 + m["cagrPct"] / 100) ** yr
                if m.get("expansionPct"):
                    pk *= (1 + m["expansionPct"] / 100)
                pk *= asmp.get("pen", 1)
            elif "regions" in m:
                addr = tam_of(m)
                if m.get("cagrPct"):
                    yr = (m.get("peakYear", 2033) - 2026)
                    addr *= (1 + m["cagrPct"] / 100) ** yr
                if m.get("expansionPct"):
                    addr *= (1 + m["expansionPct"] / 100)
                pk = addr * ((m.get("penPct", 0) or 0) / 100) * asmp.get("pen", 1)
            elif m.get("patientsK"):
                pk = m["patientsK"] * m["pricingK"] * (m.get("penPct", 0) / 100) * asmp.get("pen", 1)
            comp = (asmp.get("pos", 0) / 100) * (asmp.get("apr", 0) / 100)
            ra = pk * comp
            if is_sotp:
                pipe_ra += ra
            total_ra += ra
            total_gross += pk

    dM = 1 - (val.get("dil", 0) or 0) / 100

    if is_sotp:
        c_ev = val.get("commercialRevM", 0) * val.get("commercialMult", 1)
        yr = 2031 - 2026
        df = (1 + val["pipelineDR"] / 100) ** yr
        p_ev = (pipe_ra * val.get("pipelineMult", 1)) / df
        m_ev = 0  # milestones only for single special asset; ignored in generic path
        ev = c_ev + p_ev + m_ev + (co.get("cash") or 0)
    else:
        can = total_ra * ((val.get("cannib", 0) or 0) / 100)
        net = total_ra - can
        yr = 2033 - 2026
        df = (1 + val["dr"] / 100) ** yr
        pa = (val.get("plat", 0) + val.get("exus", 0)) * (net / total_gross) if total_gross > 0 else 0
        ev = (net * val["mult"] + pa) / df + (co.get("cash") or 0)

    tp = (ev / co["sharesOut"]) * dM
    return tp


def compute_all_scenarios(cfg):
    """Returns {scenario_key: tp} + weighted_tp."""
    results = {}
    wts = []
    tps = []
    for sk in SCENARIO_ORDER:
        tp = compute_tp(cfg, sk)
        results[sk] = tp
        w = cfg.get("scenarios", {}).get(sk, {}).get("wt", 0)
        if tp is not None:
            wts.append(w)
            tps.append(tp)
    tw = sum(wts) or 1
    weighted = sum(t * w / tw for t, w in zip(tps, wts))
    results["_weighted"] = weighted
    return results
