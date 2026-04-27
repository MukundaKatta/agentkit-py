"""agentkit re-exports all 5 libraries; verify the public surface."""

import agentkit


def test_re_exports_all_five_libraries():
    # agentfit
    assert callable(agentkit.fit)
    assert callable(agentkit.count)
    # agentguard
    assert callable(agentkit.policy)
    assert callable(agentkit.check)
    # agentsnap
    assert callable(agentkit.record)
    assert callable(agentkit.trace_tool)
    # agentvet
    assert callable(agentkit.vet)
    assert callable(agentkit.validate)
    # agentcast
    assert callable(agentkit.cast)
    assert callable(agentkit.extract_json)


def test_disambiguated_adapters():
    assert agentkit.vet_adapters is not agentkit.cast_adapters


def test_version():
    assert isinstance(agentkit.VERSION, str)
    assert agentkit.VERSION.count(".") == 2


def test_error_classes():
    assert issubclass(agentkit.OverBudgetError, Exception)
    assert issubclass(agentkit.PolicyViolation, Exception)
    assert issubclass(agentkit.ToolArgError, Exception)
    assert issubclass(agentkit.CastError, Exception)


def test_count_works():
    assert agentkit.count("hello world") > 0
