import db


# TODO avoid SQL Injection
def list_restaurants():
    restaurants = db.run("select * from restaurants")
    return [{"id": id, "name": name} for (id, name) in restaurants]


def add_restaurant(name):
    db.run("""
        insert into restaurants (name)
        values (%s)
        """, (name,))
    return


def get_menu(restaurant_id):
    menu = db.run("""
        select name, price
        from items
        where restaurant_id = %s
        """, (restaurant_id,))
    return [{"name": name, "price": price} for (name, price) in menu]


def add_item_to_menu(restaurant_id, name, price):
    db.run("""
        insert into items (restaurant_id, name, price)
        values (%s, %s, %s)
        """, (restaurant_id,name,price))
    return


def list_ordered_items(restaurant_id, table_id):
    items = db.run("""
        select i.name as name, o.creation_time as creation_time
        from orders o
        left join items i on i.id = o.item_id
        where o.restaurant_id = %s
        and o.table_id = %s
        and o.is_paid = false
        """,(restaurant_id,table_id))
    return [{"name": name, "creation_time": creation_time} for (name, creation_time) in items
]


def order_item(restaurant_id, table_id, item_id):
    db.run("""
        insert into orders (restaurant_id, table_id, item_id)
        values (%s, %s, %s)
        """,(restaurant_id,table_id,item_id))
    return

def get_bill(restaurant_id, table_id):
    amount = db.run("""select sum(i.price)
    from orders o left join items i on i.id = o.item_id
    where o.is_paid = FALSE
    and o.restaurant_id = %s
    and o.table_id = %s
    """,(restaurant_id,table_id))
    return amount


def pay(restaurant_id, table_id):
    db.run("""
    update orders
    set is_paid = true
    where restaurant_id = %s
    and table_id = %s
    """,(restaurant_id,table_id))
    return
