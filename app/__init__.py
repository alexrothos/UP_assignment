from flask import Flask
from routes import routes
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
