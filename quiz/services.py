import requests
from sqlalchemy.orm.exc import NoResultFound


def record_data_in_db(queryset: list, count: int) -> None:
    from models import QuizQuestion
    from app import db

    for i in queryset[0]:
        flag = check_query_in_db(i['id'])
        if flag:
            get_question(count)
            break
        else:
            new_question = QuizQuestion(id_question=i['id'],
                                        question=i['question'],
                                        answer=i['answer'],
                                        created_date=i['created_at'])
            db.session.add(new_question)
            return db.session.commit()


def get_question(count: int) -> None:
    parsing_data = []
    response = requests.get(f'https://jservice.io/api/random?count={count}')
    parsing_data.append(response.json())
    return record_data_in_db(parsing_data, count)


def check_query_in_db(count: int) -> bool:
    from models import QuizQuestion

    try:
        QuizQuestion.query.filter(QuizQuestion.id_question == count).one()
    except NoResultFound:
        return False
    return True


def last_question_for_output(last_question) -> tuple:
    new_return = {}
    new_return['id_question'] = last_question.id_question
    new_return['question'] = last_question.question
    new_return['answer'] = last_question.answer
    new_return['created_at'] = str(last_question.created_date)
    return new_return


def return_last_question() -> None:
    from models import QuizQuestion

    try:
        last_question = QuizQuestion.query.order_by(
            QuizQuestion.id.desc()).first()
        return last_question_for_output(last_question)
    except NoResultFound:
        return NoResultFound
