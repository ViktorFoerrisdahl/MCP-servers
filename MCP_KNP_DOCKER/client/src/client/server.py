#imports
from mcp.server.mcpserver import MCPServer
import json
import requests
import os
import logging
import httpx

#server created
mcp = MCPServer("GetWeatherFromSkjern")

# restionio server from KNP
BASE_URL = os.getenv("KNP_SERVER_URL", "http://127.0.0.1:8080")

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


@mcp.tool()
def InsertNewWeatherMeasurement(data: dict) -> str:
    """
    This tool allows an LLM to input a weather measurement into KNP weather server using POST

    Args:
    The JSON strukture in the server for at measurement looks lige this:
    {
        "id": "32",
        "date": "21021223",
        "time": "16:00",
        "place": {
            "Placename": "Arrhus",
            "Latitude": 55.939998626708984,
            "Longitude": 8.489999771118164
        },
        "temperature": 10.199999809265137,
        "humidity": 23.0
    }

    An ID should be provided by the user, as the server cant handle automating the ID's

    Returns:
    HTTP response (200 ok)

    """

    try:
        response = requests.post(f"{BASE_URL}/weather/insert", json=data, timeout=5)

        response.raise_for_status()

        return f"{response.status_code}: {response.text}"

    except Exception as e:
        return f"Fejl: {type(e).__name__}: {e}"

if __name__ == '__main__':
    mcp.run(transport="sse", host="127.0.0.1", port=8000)