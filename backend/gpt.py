from flask import Flask, jsonify, make_response, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, doc="/docs")

@api.route("/hello")
class Hello(Resource):
    def get(self):
        message = {
            "message": "Hello world."
        }
        return message, 200

if __name__ == "__main__":
    app.run(debug=True)