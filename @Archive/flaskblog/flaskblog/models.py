from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post', backref='author', lazy=True)

    # def get_reset_token(self, expires_sec=1800):
    #     s=Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s=Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id=s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    def get_reset_token(self):
        s=Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id=s.loads(token,expires_sec)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'password': self.password, 'image_file': self.image_file}

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'content': self.content, 'user_id': self.user_id}

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


class AuditLog(db.Model):
    __tablename__ = 'audit_log'
    id = db.Column(db.Integer, primary_key=True)
    action_type = db.Column(db.String(20))
    time_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    old_data = db.Column(db.JSON, default=dict)
    new_data = db.Column(db.JSON, default=dict)

    def __repr__(self):
        return f"AuditLog('{self.id}')"
