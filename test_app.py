from app import app


def client():
    return app.test_client()


def test_returns_success(client):
    response = client.get('/api/upper/foo')
    assert response.status_code == 200


def test_returns_json(client):
    response = client.get('/api/upper/foo')
    assert response.content_type == 'application/json'


def test_upper_casing_works_for_lower_case(client):
    response = client.get('/api/upper/foo')
    result = response.get_json()["result"]
    assert result == "FOO"


def test_upper_casing_works_for_mixed_case(client):
    response = client.get('/api/upper/someCamelCase')
    result = response.get_json()["result"]
    assert result == "SOMECAMELCASE"


def test_lower_returns_proper_status(client):
    response = client.get('/api/lower/WhoCares')
    assert response.status_code == 200


def test_lower_returns_json(client):
    response = client.get('/api/lower/willItBeJSON')
    assert response.content_type == 'application/json'


def test_lower_casing_works_for_all_caps(client):
    response = client.get('/api/lower/BAR')
    validity = response.get_json()
    result = response.get_json()["result"]
    assert result == "bar"


def test_lower_casing_works_for_mixed_case(client):
    response = client.get('/api/lower/MixedCaseString')
    validity = response.get_json()
    result = response.get_json()["result"]
    assert result == "mixedcasestring"