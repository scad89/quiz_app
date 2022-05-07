from flask import request
from services import get_question, return_last_question
from flask_restful import Resource


class QuestionView(Resource):
    def post(self):
        data = request.get_json()
        get_question(data["questions_num"])
        last_question = return_last_question()
        return last_question
