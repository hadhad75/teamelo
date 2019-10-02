from flask import request, jsonify

# API pour commercial
def commercial_route(app):
    # url REST
    url = "/api/commerciaux"

    # @app.route(url,  methods=['GET'])
    # def all_commercial():
    #     result = []
    #     return jsonify({"result": result}), 200


    # @app.route(url+ '/<id>',  methods=['GET'])
    # def by_id(id):
    #     result = []
    #     return jsonify({"result": result}), 200


    # @app.route(url+'/<name>',  methods=['GET'])
    # def find_by_name(name):
    #     result = ""
    #     return jsonify({"result": result}), 200

    # @app.route(url, methods=['POST'])
    # def create():
    #     restaurant = {
    #         'name': test
    #     }
    #     return jsonify(restaurant), 200
