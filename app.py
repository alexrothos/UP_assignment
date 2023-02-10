from flask import Flask
from routes import routes

app = Flask(__name__)
app.use(routes)


if __name__ == '__main__':
    app.run(debug=True)
