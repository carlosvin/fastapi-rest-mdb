serve:
	poetry run uvicorn fastapi_rest_mdb.app.main:app

dev:
	poetry run uvicorn fastapi_rest_mdb.app.main:app --reload

