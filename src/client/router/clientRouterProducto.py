from flask import Blueprint
from src.client.controller.clientControllerProducto import ClientControllerProducto
crp= Blueprint('crp', __name__)
crp.route('/crp/<idCat>', methods=['GET'])(ClientControllerProducto.onGetClientControllerProductoList)