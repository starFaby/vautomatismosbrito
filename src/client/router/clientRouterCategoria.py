from flask import Blueprint
from src.client.controller.clientControllerCategoria import ClientControllerCategoria
crc= Blueprint('crc', __name__)
crc.route('/crc', methods=['GET', 'POST'])(ClientControllerCategoria.onGetClientControllerCategoriaList) 