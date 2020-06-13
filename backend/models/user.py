from backend.config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    user_role = db.Column(db.String(50), default="user")
    password = db.Column(db.String(50))
    
    def __str__(self):
        return self.name
    
    @classmethod
    def find_by_email(cls, email:str):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_id(cls, id:int):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all_users(cls):
        return cls.query.all()
    
    def save_to_database(self) -> None:
        db.session.add(self)
        db.session.commit()

    def remove_from_database(self) -> None:
        db.session.delete(self)
        db.session.commit()