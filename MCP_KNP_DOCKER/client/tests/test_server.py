from unittest.mock import patch

import httpx

from client.server import getLatestThreeWeather


def test_weather_returnerer_liste():
    mock_response = httpx.Response(200, json=[{"temp": 12}])
    with patch("httpx.get", return_value=mock_response):
        result = getLatestThreeWeather()
    assert isinstance(result, list)
