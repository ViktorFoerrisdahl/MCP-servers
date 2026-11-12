#imports
from mcp.server.mcpserver import MCPServer
import json
import requests
import os
import logging

#server created
mcp = MCPServer("GetWeatherFromSkjern")

# restionio server from KNP
BASE_URL = os.getenv("KNP_SERVER_URL")

#create tooL
@mcp.tool()
def getLatestThreeWeather() -> dict:
    """
    This tool returns the three latest inputs from the weather server

    Args:
    No arguments needed

    Returns:
    three json objects

    """
    response = requests.get(f"{BASE_URL}/weather/latest", timeout=5)

    return response.json()

@mcp.tool()
def getWeahterWithSpecificID(weather_id: int) -> dict:
    """
    This tool returns the weather information from a specific ID

    Args:
    weather_id is the desired ID to get weather information from.

    Returns:
    one json object

    """

    response = requests.get(f"{BASE_URL}/weather/id/{weather_id}", timeout=5)

    return response.json()


if __name__ == '__main__':
    mcp.run(transport="stdio")