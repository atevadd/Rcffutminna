from main_app import db
from datetime import datetime

#message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    minister = db.Column(db.String(50))
    title = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.Text, nullable=False)
    audio = db.Column(db.String(100))
    
    def __str__(self):
        return f"Message('{self.minister}', '{self.title}')"
    
    @classmethod
    def find_by_title(cls, title:str):
        return cls.query.filter_by(title=title).first()
    
    @classmethod
    def find_by_id(cls, id:int):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_minister(cls, minister:str):
        return cls.query.filter_by(minister=minister).first()
    
    def save_to_database(self) -> None:
        db.session.add(self)
        db.session.commit()

    def remove_from_database(self) -> None:
        db.session.delete(self)
        db.session.commit()

#Announcement model
class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    annouce = db.Column(db.String(50))
    image = db.Column(db.String(50), default="default.jpg")
    content = db.Column(db.Text, nullable=False)
    
    @classmethod
    def find_by_id(cls, id:int):
        return cls.query.filter_by(id=id).first()
    
    def save_to_database(self) -> None:
        db.session.add(self)
        db.session.commit()

    def remove_from_database(self) -> None:
        db.session.delete(self)
        db.session.commit()
