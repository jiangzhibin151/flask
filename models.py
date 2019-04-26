from db import db


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), unique=True, index=True)
    content = db.Column(db.Text, index=True)
    time = db.Column(db.TIMESTAMP, index=True)
    name = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True)

    def __init__(self, title, content, time, name, category):
        self.title = title
        self.content = content
        self.time = time
        self.name = name
        self.category = category

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name