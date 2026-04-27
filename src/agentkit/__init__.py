"""agentkit -- the agent reliability stack in one install.

Re-exports the most-used surfaces of all 5 sibling libraries so a typical
agent application only needs one import line. For the full surface of any
one library, import it directly:

    from agentfit import fit, count, OverBudgetError
    from agentguard import policy, check, PolicyViolation
    from agentsnap import record, trace_tool, expect_snapshot, diff
    from agentvet import vet, validate, adapters, ToolArgError
    from agentcast import cast, extract_json, adapters, CastError

agentkit just makes the common case ergonomic.
"""

from agentfit import count, fit, OverBudgetError
from agentguard import policy, check, PolicyViolation
from agentsnap import record, trace_tool, expect_snapshot, diff
from agentvet import vet, validate, ToolArgError
from agentcast import cast, extract_json, CastError

# Adapters from vet and cast collide on the symbol name; re-export both
# under disambiguated names.
from agentvet import adapters as vet_adapters
from agentcast import adapters as cast_adapters

__version__ = "0.1.0"
VERSION = __version__

__all__ = [
    "count", "fit", "OverBudgetError",
    "policy", "check", "PolicyViolation",
    "record", "trace_tool", "expect_snapshot", "diff",
    "vet", "validate", "ToolArgError", "vet_adapters",
    "cast", "extract_json", "CastError", "cast_adapters",
    "VERSION",
]
