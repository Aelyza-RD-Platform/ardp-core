"""
Tests pour {{ cookiecutter.project_name }}
"""

import pytest
from {{ cookiecutter.server_name }}.server import server, list_tools, call_tool


@pytest.mark.asyncio
async def test_list_tools():
    """Test de la liste des outils"""
    tools = await list_tools()
    assert len(tools) > 0
    assert any(tool.name == "example_tool" for tool in tools)


@pytest.mark.asyncio
async def test_call_example_tool():
    """Test d'appel d'un outil"""
    result = await call_tool("example_tool", {"input": "test"})
    assert len(result) > 0
    assert result[0].text == "Résultat pour: test"
