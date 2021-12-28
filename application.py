import flask
from flask import Flask
from flask import request
import data_access

application = Flask(__name__)

CONTENT_TYPE_JSON = {'ContentType': 'application/json'}


@application.get('/')
def hello_world():
    return 'Hello World'
    pass


@application.get('/restaurants')
def list_restaurants():
    """List restaurants  AUTHORIZED USER ONLY. Separate API?"""
    rv = flask.jsonify(data_access.list_restaurants())
    return rv, 200, CONTENT_TYPE_JSON


@application.post('/restaurants')
def add_restaurant():
    """Add new restaurant  AUTHORIZED USER ONLY. Separate API?"""
    content = request.get_json()
    if "name" not in content:
        return "Bad Request", 400
    data_access.add_restaurant(content["name"])
    return "Created", 201


@application.get('/restaurants/<int:rest_id>')
def get_menu(rest_id):
    """Get restaurant menu"""
    rv = flask.jsonify(data_access.get_menu(rest_id))
    return rv, 200, CONTENT_TYPE_JSON


@application.post('/restaurants/<int:rest_id>')
def add_item_to_menu(rest_id):
    """Add item to menu  AUTHORIZED USER ONLY. Separate API?"""
    content = request.get_json()
    if not {"name","price"}.issubset(content.keys()):
        return "Bad Request", 400
    data_access.add_item_to_menu(rest_id,content["name"], content["price"])
    return "Created", 201


@application.get('/restaurants/<int:rest_id>/tables/<table_id>')
def list_ordered_items(rest_id, table_id):
    """List ordered items from table"""
    rv = flask.jsonify(data_access.list_ordered_items(rest_id, table_id))
    return rv, 200, CONTENT_TYPE_JSON


@application.post('/restaurants/<int:rest_id>/tables/<table_id>')
def order_item(rest_id, table_id):
    """Order new item to table"""
    content = request.get_json()
    if not "item_id" in content:
        return "Bad Request", 400
    data_access.order_item(rest_id, table_id, content["item_id"])
    return "Created", 201


@application.get('/restaurants/<int:rest_id>/tables/<table_id>/pay')
def get_bill(rest_id, table_id):
    """Is table free? / All is paid?"""
    rv = flask.jsonify(data_access.get_bill(rest_id, table_id))
    return rv, 200, CONTENT_TYPE_JSON


@application.post('/restaurants/<int:rest_id>/tables/<table_id>/pay')
def pay(rest_id, table_id):
    """Pay full amount  AUTHORIZED USER ONLY. Separate API?"""
    content = request.get_json()
    if not "pay" in content:
        return "Bad Request", 400
    bill = data_access.get_bill()
    if content["pay"] is not bill:
        return "Conflict", 409
    data_access.pay(rest_id, table_id)
    return "Accepted", 202








#application.run()
