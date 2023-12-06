from flask import render_template as render, request, flash, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from src.client.services.clientServiceProducto import ClientServiceProducto

class ClientControllerProducto:

    def onGetClientControllerProductoList(idCat):
        try:
            consulta = ClientServiceProducto.ongetClientServiceProducto(idCat)
            if consulta != []:
                flash('Productos Listadas', category='success')
                return render("client/clientProductoView.html", consulta=consulta)
            else:
                flash('No existe Productos', category='success')
                return render("client/clientProductoView.html", consulta=consulta)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)