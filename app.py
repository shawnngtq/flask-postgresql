import os

from flask import Flask
from flask_migrate import Migrate

from models import db

# set environment variables
os.system("ls")
os.system("APP_SETTINGS='config.DevelopmentConfig'")
os.environ["APP_SETTINGS"] = "config.DevelopmentConfig"

# set app
app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
db.init_app(app)
migrate = Migrate(app, db)


# define route
@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run()
