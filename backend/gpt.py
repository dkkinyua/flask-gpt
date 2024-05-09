import os
from openai import OpenAI
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from dotenv import load_dotenv

load_dotenv()

prompt_model = {
    "prompt": fields.String()
}

app = Flask(__name__)
api = Api(app, doc="/docs")
gpt = OpenAI(
    api_key=os.getenv("API_KEY")
)

@api.route("/hello")
class Hello(Resource):
    def get(self):
        message = {
            "message": "Hello world."
        }
        return message, 200

@api.route("/chat")
class Chat(Resource):
    @api.expect(prompt_model)
    def post(self):
        try:
            prompt = request.json.get("prompt")

            response = gpt.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            ai_response = response.choices[0].message.content

            return jsonify({"ai_response": ai_response}), 200

        except Exception as e:
            return jsonify({"error": f"An error occurred: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
