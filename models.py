from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy(app)
ma = Marshmallow(app)


# TODO: Need to create association tables and relationships for restaurant-menu and menu-items

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restname = db.Column(db.String(80), unique=False)
    cuisines = db.Column(db.String(120), unique=False)
    addr = db.Column(db.String(120), unique=False)

    def __init__(self, restname, cuisines, addr):
        self.restname = restname
        self.cuisines = cuisines
        self.addr = addr


class RestaurantSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('restname', 'cuisines', 'addr')


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), unique=True)

    def __init__(self, type):
        self.type = type


class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ['type']


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(30), unique=True)

    def __init__(self, item):
        self.item = item

class ItemSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ['item']


restaurant_schema = RestaurantSchema()
restaurant_schemas = RestaurantSchema(many=True)

menu_schema = MenuSchema()
menu_schemas = MenuSchema(many=True)

item_schema = ItemSchema()
item_schemas = ItemSchema(many=True)