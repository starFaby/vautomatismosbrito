from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class ClientServiceProducto:
    
    @classmethod
    def ongetClientServiceProducto(self, idCat):
        try:
            productoList = Producto.query.filter(Producto.pfsabprodestado == 1).filter(Producto.pfsabcategoriaid == idCat)
            return productoList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)