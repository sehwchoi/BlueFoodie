from flask import Flask, request, jsonify
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

from models import *

#db.drop_all()
db.create_all()

# endpoint to create new restaurant
@app.route("/")
def index():
    return "BlueFoodie!!"

# endpoint to create new restaurant
@app.route("/restaurant", methods=["POST"])
def add_restaurant():
    restname = request.json['restname']
    cuisines = request.json['cuisines']
    addr = request.json['addr']

    new_restaurant = Restaurant(restname, cuisines, addr)

    db.session.add(new_restaurant)
    db.session.commit()

    # return jsonify(new_restaurant)
    return restaurant_schema.jsonify(new_restaurant)

# endpoint to show all restaurant
@app.route("/restaurant", methods=["GET"])
def get_restaurant():
    all_restaurant = Restaurant.query.all()
    result = restaurant_schemas.dump(all_restaurant)
    return jsonify(result.data)

# endpoint to get restaurant detail by id
@app.route("/restaurant/<id>", methods=["GET"])
def restaurant_detail(id):
    restaurant = Restaurant.query.get(id)
    return restaurant_schema.jsonify(restaurant)

# endpoint to delete restaurant
@app.route("/restaurant/<id>", methods=["DELETE"])
def restaurant_delete(id):
    restaurant = Restaurant.query.get(id)
    db.session.delete(restaurant)
    db.session.commit()

    return restaurant_schema.jsonify(restaurant)


@app.route("/menu", methods=["POST"])
def add_menu():
    type = request.json['type']

    new_menu = Menu(type)

    db.session.add(new_menu)
    db.session.commit()

    return jsonify(type)

@app.route("/menu", methods=["GET"])
def get_menu():
    all_menu = Menu.query.all()
    result = menu_schemas.dump(all_menu)
    return jsonify(result.data)

@app.route("/menu/<id>", methods=["DELETE"])
def menu_delete(id):
    menu = Menu.query.get(id)
    db.session.delete(menu)
    db.session.commit()

    return menu_schema.jsonify(menu)


@app.route("/item", methods=["POST"])
def add_item():
    item = request.json['item']

    new_item = Item(item)

    db.session.add(new_item)
    db.session.commit()

    return jsonify(item)

# endpoint to show all restaurant
@app.route("/item", methods=["GET"])
def get_item():
    all_item = Item.query.all()
    result = item_schemas.dump(all_item)
    return jsonify(result.data)

# endpoint to delete restaurant
@app.route("/item/<id>", methods=["DELETE"])
def item_delete(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return item_schema.jsonify(item)


if __name__ == '__main__':
    app.run(debug=True)