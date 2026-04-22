---
description: Run all three CI checks locally (schema + audit + snapshot) and summarize
---

# Full config audit

Run all three validation tools and produce a single summary.

```bash
py scripts/ops/validate_schema.py
py scripts/ops/audit_configs.py
py scripts/ops/snapshot_scenarios.py
```

Summarize the output as:

```
SCHEMA:   <pass/fail> — <N configs>, <errors>
AUDIT:    CRIT=<n> FLAG=<n> WARN=<n>
SNAPSHOT: <OK | N fails | N warns>
```

If any tool reports issues, list the top offenders (first 5 per category)
and suggest the fix path:
- Schema errors → point to the specific property
- Audit CRIT → SOM > TAM or SOM < sales violations
- Audit FLAG → aspirational SOM or miscalibrated scenario shape
- Snapshot drift → run `py scripts/ops/snapshot_scenarios.py --update` if intentional

Do not modify any config. Read-only.
