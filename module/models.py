from module import db
from sqlalchemy.sql import func

class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="user", lazy="dynamic")

class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    is_general = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer)

    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")

class RecordModel(db.Model):
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), unique=False, nullable=True)
    creation_time = db.Column(db.TIMESTAMP, server_default=func.now())
    expenses = db.Column(db.Integer, unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")