from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str(required=True)

class CategorySchema(Schema):
    name = fields.Str(required=True)
    user_id = fields.Int()

class RecordSchema(Schema):
    user_id = fields.Int()
    category_id = fields.Int()
    creation_time = fields.DateTime()
    expenses = fields.Int(required=True)

class RecordQuerySchema(Schema):
    user_id = fields.Str()
    category_id = fields.Str()