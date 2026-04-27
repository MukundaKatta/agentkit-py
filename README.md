# agentkit-py

**The agent reliability stack in one install** — Python.

```bash
pip install agentkit-py
```

```python
from agentkit import fit, policy, check, record, vet, cast
```

## What's in the box

| Symbol | From | What it does |
|---|---|---|
| `fit`, `count`, `OverBudgetError` | [`agentfit-py`](https://pypi.org/project/agentfit-py/) | Fit messages into a token budget |
| `policy`, `check`, `PolicyViolation` | [`agentguard-firewall`](https://pypi.org/project/agentguard-firewall/) | Network-egress firewall for tools |
| `record`, `trace_tool`, `expect_snapshot`, `diff` | [`agentsnap-py`](https://pypi.org/project/agentsnap-py/) | Snapshot tests for tool-call traces |
| `vet`, `validate`, `vet_adapters`, `ToolArgError` | [`agentvet-py`](https://pypi.org/project/agentvet-py/) | Validate tool args before execution |
| `cast`, `extract_json`, `cast_adapters`, `CastError` | [`agentcast-py`](https://pypi.org/project/agentcast-py/) | Structured-output enforcer |

`adapters` from agentvet and agentcast are exposed as `vet_adapters` and `cast_adapters` to avoid the name collision.

## Pipeline

The libraries compose into a natural agent reliability pipeline — **fit → guard → snap → vet → cast**:

```
fit messages       → fit a chat history into the model's budget
firewall fetches   → block tool fetches outside the allowlist
expect_snapshot    → diff this run's tool calls against a baseline
vet args           → validate args before each tool runs
cast output        → validate the model's structured response
```

You don't have to use all five — pick the ones you need.

## Sibling

JS / TypeScript users: [`@mukundakatta/agentkit`](https://github.com/MukundaKatta/agentkit).

## License

MIT
