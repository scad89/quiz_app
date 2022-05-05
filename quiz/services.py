import requests
from sqlalchemy.orm.exc import NoResultFound


def record_data_in_db(queryset, count):
    from models import QuizQuestion
    from app import db

    for i in queryset[0]:
        flag = check_query_in_db(i['id'])    # int
        if flag:
            get_question(count)
            break
        else:
            db.create_all()
            new_question = QuizQuestion(id_question=i['id'],
                                        question=i['question'],
                                        answer=i['answer'],
                                        created_date=i['created_at'])
            db.session.add(new_question)
            return db.session.commit()


def get_question(count):
    parsing_data = []
    response = requests.get(f'https://jservice.io/api/random?count={count}')
    parsing_data.append(response.json())
    return record_data_in_db(parsing_data, count)


def check_num(num):
    if num.isdigit():
        return int(num)
    else:
        return False


def check_query_in_db(id_question):
    from models import QuizQuestion
    from app import db
    try:
        db.session.query(QuizQuestion.id_question).filter_by(
            id_question=id_question).one()
    except NoResultFound:
        return False
    return True


def return_last_question():
    from models import QuizQuestion
    from app import db
    try:
        return db.session.query(QuizQuestion.id,
                                QuizQuestion.id_question,
                                QuizQuestion.question,
                                QuizQuestion.answer,
                                QuizQuestion.created_date).order_by(QuizQuestion.id.desc()).first()
    except NoResultFound:
        return NoResultFound
