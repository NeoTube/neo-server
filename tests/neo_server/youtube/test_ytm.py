import pytest

from neo_server.youtube.ytm import YtmCommands


@pytest.fixture
def ytm_commands() -> YtmCommands:
    return YtmCommands()


def test_search_not_none(ytm_commands: YtmCommands) -> None:
    """Basic Test."""
    search_query = "The Beatles"
    max_results = 4
    search_items = ytm_commands.search(search_query, max_results)
    assert search_items is not None
