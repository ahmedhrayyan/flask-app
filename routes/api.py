from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/message")
def message():
    return {"message": "Hello World!"}
