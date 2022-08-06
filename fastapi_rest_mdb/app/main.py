from fastapi_rest_mdb.app.settings import Settings
from fastapi_rest_mdb.app.app import App

app = App(Settings()).app
