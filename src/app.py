from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# don't pass in the app object yet
db = SQLAlchemy()

def create_app(db_config: str) -> Flask:
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = db_config
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app

app = create_app('sqlite:///production.db')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
