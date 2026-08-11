# Integrated tool triggers (Python 3.8 legacy source)

All 14 manifests analyze the real legacy WSGI service, tests, dependencies, or
Git history in an isolated Python 3.10+ analyzer environment.

| # | Trigger | Tool(s) | Project input | Purpose |
|---:|---|---|---|---|
| 1 | `beniget` | Beniget | `legacy_api/**/*.py` | Def-use/data flow |
| 2 | `cognitive-ast` | complexipy | `legacy_api/**/*.py` | Cognitive complexity |
| 3 | `cosmic-ray` | Cosmic Ray | service + API tests | Mutation testing |
| 4 | `coverage-py` | coverage.py | service + tests | Statement/branch coverage |
| 5 | `coverage-py-beniget` | coverage.py + Beniget | service + tests | Coverage plus data flow |
| 6 | `crosshair` | CrossHair | schema + service | Symbolic path analysis |
| 7 | `jscpd` | jscpd | service + tests | Duplicate detection |
| 8 | `pip-audit` | pip-audit | dependency files | Vulnerability audit |
| 9 | `pydriller` | PyDriller | Git history | Churn/history analysis |
| 10 | `pylint` | Pylint | service + tests | Static lint analysis |
| 11 | `pymcdc` | pymcdc | dispatcher + tests | Decision coverage |
| 12 | `radon-lizard` | Radon + Lizard | service source | Complexity analysis |
| 13 | `semgrep-bandit` | Semgrep + Bandit | service source | Security SAST |
| 14 | `testmon` | pytest-testmon | service + tests | Change-aware tests |

Every manifest declares Python 3.8 source, its exact project targets, and an
executable command. There are no disconnected sample fixtures.
