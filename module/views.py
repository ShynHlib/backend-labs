import uuid
from flask import Flask, jsonify, request
from datetime import date

app = Flask(__name__)
users = {}
categories = {}
records = {}


@app.get("/user/<user_id>")
def get_user(user_id):
    if user_id in users.keys():
        return users[user_id], 200
    else:
        return jsonify({"Error":"No user with this id"}), 400

@app.delete("/user/<user_id>")
def delete_user(user_id):
    if user_id in users.keys():
        user = users[user_id]
        del users[user_id]
        return jsonify(user), 200
    else:
        return jsonify({"Error":"No user with this id"}), 400

@app.post("/user")
def add_user():
    user_name = request.args.get("name")
    user_id = uuid.uuid4().hex
    user = {
        "id": user_id,
        "name": user_name
    }
    users[user_id] = user
    return user, 200

@app.get("/users")
def get_users():
    return jsonify(list(users.values())), 200

@app.get("/category")
def get_category():
    category_id = request.args.get("id")
    if category_id in categories.keys():
        return categories[category_id], 200
    else:
        return jsonify({"Error":"No category with this id"}), 400

@app.post("/category")
def add_category():
    category_name = request.args.get("name")
    category_id = uuid.uuid4().hex
    category = {
        "id": category_id,
        "name": category_name
    }
    categories[category_id] = category
    return category, 200

@app.delete("/category")
def delete_category():
    category_id = request.args.get("id")
    if category_id in categories.keys():
        category = categories[category_id]
        del categories[category_id]
        return jsonify(category), 200
    else:
        return jsonify({"Error":"No category with this id"}), 400

@app.get("/categories")
def get_categories():
    return jsonify(list(categories.values())), 200

@app.get("/record/<record_id>")
def get_record(record_id):
    if record_id in records.keys():
        return records[record_id], 200
    else:
        return jsonify({"Error":"No record with this id"}), 400

@app.delete("/record/<record_id>")
def delete_record(record_id):
    if record_id in records.keys():
        record = records[record_id]
        del records[record_id]
        return jsonify(record), 200
    else:
        return jsonify({"Error":"No record with this id"}), 400

@app.post("/record")
def add_record():
    record_id = uuid.uuid4().hex
    record = {
        "id": record_id,
        "user_id": request.args.get("user_id"),
        "category_id": request.args.get("category_id"),
        "creation_time": date.today(),
        "expenses": request.args.get("expenses")
    }
    records[record_id] = record
    return record, 200

@app.get("/record")
def filter_records():
    category_id = request.args.get('category_id')
    user_id = request.args.get('user_id')
    res = []

    if not category_id and not user_id:
        return jsonify({"Error": "Provide at least one argument: category_id or user_id"}), 400

    for record in records.values():
        match_category = record["category_id"] == category_id if category_id else True
        match_user = record["user_id"] == user_id if user_id else True

        if match_category or match_user:
            res.append(record)

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
