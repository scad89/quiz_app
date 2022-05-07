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
            print()
            # db.create_all()
            # new_question = QuizQuestion(id_question=i['id'],
            #                             question=i['question'],
            #                             answer=i['answer'],
            #                             created_date=i['created_at'])
            # db.session.add(new_question)
            # return db.session.commit()


def get_question(count: int) -> None:
    parsing_data = []
    response = requests.get(f'https://jservice.io/api/random?count={count}')
    parsing_data.append(response.json())
    return record_data_in_db(parsing_data, count)


def check_query_in_db(id_question: int) -> bool:
    from models import QuizQuestion
    from app import db
    try:
        db.session.query(QuizQuestion.id_question).filter_by(
            id_question=id_question).one()
    except NoResultFound:
        return False
    return True


def last_question_to_str(last_question) -> tuple:
    new_return = []
    for i in last_question:
        new_return.append(str(i))
    return tuple(new_return)


def return_last_question() -> None:
    from models import QuizQuestion
    from app import db
    try:
        last_question = db.session.query(QuizQuestion.id,
                                         QuizQuestion.id_question,
                                         QuizQuestion.question,
                                         QuizQuestion.answer,
                                         QuizQuestion.created_date).order_by(QuizQuestion.id.desc()).first()
        return last_question_to_str(last_question)
    except NoResultFound:
        return NoResultFound
