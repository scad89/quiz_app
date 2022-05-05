from flask import render_template, request, Blueprint
from services import get_question, check_num, record_data_in_db, return_last_question


app_route = Blueprint('route', __name__)


@app_route.route('/')
def main():
    return render_template('index.html')


@app_route.route('/question', methods=["POST"])
def rate():
    number = request.form.get('number')
    int_num = check_num(number)
    if int_num:
        response = get_question(int_num)
        record_data_in_db(response)
        last_question = return_last_question()
        return render_template('question.html', last_question=last_question)
    else:
        return render_template('error_num.html')
