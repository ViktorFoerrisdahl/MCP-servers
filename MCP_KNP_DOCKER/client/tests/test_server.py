import responses

from client.server import getLatestThreeWeather


@responses.activate
def test_weather_returnerer_tre():
    responses.add(
        responses.GET,
        "http://host.docker.internal:8080/weather/latest",
        json=[{"temp": 12}, {"temp": 11}, {"temp": 10}],
        status=200,
    )

    result = getLatestThreeWeather()

    assert len(result) == 3
