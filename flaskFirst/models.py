from flaskFirst import db


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"Quote('{self.id}', '{self.text}', '{self.author}')"
