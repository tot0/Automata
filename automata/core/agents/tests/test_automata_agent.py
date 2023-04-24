import pytest

from automata.core import load_llm_toolkits
from automata.core.agents.automata_agent import AutomataAgent
from automata.core.utils import root_py_path
from automata.tools.python_tools.python_indexer import PythonIndexer


@pytest.fixture
def automata_agent():
    python_indexer = PythonIndexer(root_py_path())

    tool_list = ["python_indexer"]
    mock_llm_toolkits = load_llm_toolkits(tool_list)

    overview = python_indexer.get_overview()

    initial_payload = {
        "overview": overview,
    }

    agent = AutomataAgent(
        initial_payload=initial_payload,
        instructions="Test instruction.",
        llm_toolkits=mock_llm_toolkits,
    )
    return agent


def test_automata_agent_init(automata_agent):
    assert automata_agent is not None
    assert automata_agent.model == "gpt-4"
    assert automata_agent.session_id is not None
    assert len(automata_agent.toolkits.keys()) > 0


def test_automata_agent_iter_task(
    automata_agent,
):
    assert len(automata_agent.messages) == 3
