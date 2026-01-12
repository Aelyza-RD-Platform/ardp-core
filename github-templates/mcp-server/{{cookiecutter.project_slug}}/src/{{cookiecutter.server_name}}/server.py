"""
Serveur MCP principal pour {{ cookiecutter.project_name }}
"""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configuration
SERVER_NAME = "{{ cookiecutter.server_name }}"
SERVER_VERSION = "0.1.0"

# Créer le serveur MCP
server = Server(SERVER_NAME)

{% if cookiecutter.use_postgres == "y" %}
# Configuration PostgreSQL (si nécessaire)
import os
from asyncpg import create_pool

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dbname")

async def get_db_pool():
    """Crée un pool de connexions PostgreSQL"""
    return await create_pool(DATABASE_URL)
{% endif %}

{% if cookiecutter.use_redis == "y" %}
# Configuration Redis (si nécessaire)
import redis.asyncio as redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

async def get_redis_client():
    """Crée un client Redis"""
    return await redis.from_url(REDIS_URL)
{% endif %}

@server.list_tools()
async def list_tools() -> list[Tool]:
    """Liste les outils disponibles"""
    return [
        Tool(
            name="example_tool",
            description="Exemple d'outil MCP",
            inputSchema={
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "Input pour l'outil"
                    }
                },
                "required": ["input"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Exécute un outil"""
    if name == "example_tool":
        input_value = arguments.get("input", "")
        return [
            TextContent(
                type="text",
                text=f"Résultat pour: {input_value}"
            )
        ]
    else:
        raise ValueError(f"Outil inconnu: {name}")

async def main():
    """Point d'entrée principal"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
