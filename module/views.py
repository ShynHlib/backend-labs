from flask import jsonify, request
from datetime import date
from module import app, db
from module.models import UserModel, RecordModel, CategoryModel
from module.schemas import UserSchema, RecordSchema, CategorySchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

with app.app_context():
    db.create_all()
    db.session.commit()


@app.get("/user/<user_id>")
def get_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    response = {
        "id": user.id,
        "name": user.name
    }
    return response, 200


@app.delete("/user/<user_id>")
def delete_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"Message": "User successfully deleted"}, 200


@app.post("/user")
def add_user():
    user_data = request.args
    try:
        user_valid = UserSchema().load(user_data)
    except ValidationError as error:
        return jsonify({'Error': error.messages}), 400

    user = UserModel(name=user_valid["name"])
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return jsonify({"Error": "IntegrityError"}), 400
    response = {
        "id": user.id,
        "name": user.name
    }
    return response, 200


@app.get("/users")
def get_users():
    res = []

    for user in UserModel.query.all():
        res.append({
            "id": user.id,
            "name": user.name
        })
    return jsonify(res), 200


@app.get("/category")
def get_category():
    category_id = request.args.get("id")
    category = CategoryModel.query.get_or_404(category_id)

    response = {
        "id": category.id,
        "name": category.name
    }
    return response, 200


@app.get("/categories")
def get_categories():
    user_id = request.args.get("user_id")
    res = []

    if user_id is None:
        categories = CategoryModel.query.filter_by(is_general=True).all()
    else:
        categories = CategoryModel.query.filter_by(is_general=False, user_id=user_id).all()

    for category in categories:
        res.append({
            "id": category.id,
            "name": category.name,
            "is_general": category.is_general,
        })
    return jsonify(res), 200


@app.post("/category")
def add_category():
    category_data = request.args
    categ_valid = CategorySchema()
    try:
        categ_valid = categ_valid.load(category_data)
    except ValidationError as error:
        return jsonify({'Error': error.messages}), 400

    name = categ_valid.get("name")
    user_id = categ_valid.get("user_id")

    if user_id is None:
        category = CategoryModel(name=name, is_general=True)
    else:
        category = CategoryModel(name=name, is_general=False, user_id=user_id)

    try:
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        return jsonify({"Error": "IntegrityError"}), 400
    response = {
        "id": category.id,
        "name": category.name
    }
    return response, 200

@app.delete("/category")
def delete_category():
    category_id = request.args.get("id")
    category = CategoryModel.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return {"Message": "Category successfully deleted"}

@app.get("/record/<record_id>")
def get_record(record_id):
    record = RecordModel.query.get_or_404(record_id)
    response = {
        "id": record.id,
        "user_id": record.user_id,
        "category_id": record.category_id,
        "creation_time": record.creation_time,
        "expenses": record.expenses
    }
    return response, 200

@app.delete("/record/<record_id>")
def delete_record(record_id):
    record = RecordModel.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return {"Message": "Record successfully deleted"}

@app.post("/record")
def add_record():
    record_data = request.args
    record_valid = RecordSchema()
    try:
        record_valid = record_valid.load(record_data)
    except ValidationError as error:
        return jsonify({'Error': error.messages}), 400

    if not record_valid.get("user_id") and not record_valid.get("category_id"):
        return jsonify({'Error': "Provide at least one argument: category_id or user_id" }), 400

    record = RecordModel(expenses=record_valid.get("expenses"), user_id=record_valid.get("user_id"), category_id=record_valid.get("category_id"))

    try:
        db.session.add(record)
        db.session.commit()
    except IntegrityError:
        return jsonify({"Error": "IntegrityError"}), 400
    response = {
        "id": record.id,
        "user_id": record.user_id,
        "category_id": record.category_id,
        "creation_time": record.creation_time,
        "expenses": record.expenses
    }
    return response, 200

@app.get("/record")
def filter_records():
    category_id = request.args.get('category_id')
    user_id = request.args.get('user_id')
    records = []
    res = []

    if not category_id and not user_id:
        return jsonify({"Error": "Provide at least one argument: category_id or user_id"}), 400

    if category_id and user_id:
        records = RecordModel.query.filter_by(category_id=category_id, user_id=user_id)
    else:
        if category_id:
            records = RecordModel.query.filter_by(category_id=category_id)
        if user_id:
            records = RecordModel.query.filter_by(user_id=user_id)

    for record in records:
        res.append({
            "id": record.id,
            "user_id": record.user_id,
            "category_id": record.category_id,
            "creation_time": record.creation_time,
            "expenses": record.expenses
        })

    return jsonify(res), 200

@app.route("/")
def homepage():
    response = "<p>Home page</p>"
    return response, 200

@app.route("/healthcheck")
def healthCheck():
    response = {
        'time': date.today(),
        'status': 200,
    }
    return jsonify(response), 200
