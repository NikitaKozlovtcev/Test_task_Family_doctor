import pytest


@pytest.mark.parametrize(
    "test_input, expected_code",
    [
        ({"country_code": "RU", "city": "Moscow", "date": "2022-02-08T12:00"}, 200),
        ({"country_code": "RU", "city": "Moscow", "date": "2022-02-08T12:00"}, 200),
        ({"country_code": "RU", "city": "Moscow", "date": "2022-02-09T12:00"}, 200),
        ({"country_code": "RU", "city": "Moscow", "date": "2022-02-09T12:00"}, 200),
        ({"country_code": "RU", "city": "Moscow", "date": "2022-03-09T12:00"}, 200),
        ({"country_code": "", "city": "Moscow", "date": "2022-03-09T12:00"}, 422),
        ({"country_code": "RU", "city": "", "date": "2022-03-09T12:00"}, 422),
        ({"country_code": "RU", "city": "Moscow", "date": "20223-09T12:00"}, 400),
    ]
)
def test_get_weather(test_app, test_input, expected_code):
    test_request = f'/weather?' \
                   f'country_code={test_input["country_code"]}&' \
                   f'city={test_input["city"]}&' \
                   f'date={test_input["date"]}'

    response = test_app.get(test_request)
    print('-----------------------------------------------------------')
    print(test_request)
    print(response.status_code)
    print(response.json())
    print('-----------------------------------------------------------')
    assert response.status_code == expected_code

