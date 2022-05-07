from app import db


class QuizQuestion(db.Model):
    __tablename__ = 'quizquestion'

    id = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer)
    question = db.Column(db.String(1000))
    answer = db.Column(db.String(100))
    created_date = db.Column(db.DateTime)

    def __str__(self):
        return {"id_question": self.id_question}

    def json(self):
        return {"id_question": self.id_question,
                "question": self.question,
                "answer": self.answer,
                "created_date": self.created_date}
