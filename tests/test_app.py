from fastapi_rest_mdb.app.app import App


def test_app_version():
    assert len(App.version()) > 4
