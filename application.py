from flask import Flask
application = Flask(__name__)


@application.get('/')
def hello_world():
    return 'Hello World'
    pass


@application.get('/restaurants')
def list_restaurants():
    """List restaurants  AUTHORIZED USER ONLY. Separate API?"""
    return "many restaurants" #TODO
    pass


@application.post('/restaurants')
def add_restaurant():
    """Add new restaurant  AUTHORIZED USER ONLY. Separate API?"""
    rest_id=2 #TODO return ID
    return rest_id
    pass


@application.get('/restaurants/<int:rest_id>')
def get_menu(rest_id):
    """Get restaurant menu"""
    return str(rest_id),200 #TODO
    pass


@application.post('/restaurants/<int:rest_id>')
def add_item_to_menu(rest_id):
    """Add item to menu"""
    return str(rest_id),200 #TODO
    pass


@application.get('/restaurants/<int:rest_id>/tables/<table_id>')
def list_ordered_items(rest_id, table_id):
    """List ordered items from table"""
    return str(rest_id),str(table_id),200 #TODO
    pass


@application.post('/restaurants/<int:rest_id>/tables/<table_id>')
def order_item(rest_id, table_id):
    """Order new item to table"""
    return str(rest_id),str(table_id),200 #TODO
    pass


@application.get('/restaurants/<int:rest_id>/tables/<table_id>/pay')
def get_bill(rest_id, table_id):
    """Is table free? / All is paid?"""
    return str(rest_id),str(table_id),200 #TODO
    pass


@application.post('/restaurants/<int:rest_id>/tables/<table_id>/pay')
def pay(rest_id, table_id):
    """Pay SOME amount"""
    return str(rest_id),str(table_id),200 #TODO
    pass

#application.run()
