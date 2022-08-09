from fastapi_rest_mdb.app.db import DbSettings
from fastapi_rest_mdb.app.settings import AppSettings
from fastapi_rest_mdb.app.app import App

db = DbSettings().db
app = App(AppSettings(), db).app
