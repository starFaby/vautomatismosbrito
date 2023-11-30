from flask import Blueprint
from src.admin.controller.adminControllerCategoria import AdminControllerCategoria
# admin- router - categoria
arc= Blueprint('arc', __name__)
arc.route('/arc', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerCategoria.onGetAdminControllerCategoriaList)
arc.route('/arc/<int:page>', methods=['GET', 'POST'])(AdminControllerCategoria.onGetAdminControllerCategoriaList)
arc.route('/arcs', methods=['POST'])(AdminControllerCategoria.onGetControllerAdminCategoriaSave)
arc.route('/arcupd/<id>', methods=['GET', 'POST'])(AdminControllerCategoria.onGetControllerAdminCategoriaUpdate)
arc.route('/arcdel/<id>', methods=['GET'])(AdminControllerCategoria.onGetControllerAdminCategoriaDelete)