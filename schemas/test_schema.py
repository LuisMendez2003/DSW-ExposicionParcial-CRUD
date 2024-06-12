from utils.ma import ma
from marshmallow import fields

class TestSchema(ma.Schema):
    id_test = fields.Integer()
    
    nombre = fields.String()
    
test_schema = TestSchema()
tests_schema = TestSchema(many = True)