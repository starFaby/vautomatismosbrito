from flask import render_template as render, request, flash, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from src.client.services.clientServiceCategoria import ClientServiceCategoria

class ClientControllerCategoria:

    def onGetClientControllerCategoriaList():
        try:
            categorias = ClientServiceCategoria.ongetClientServiceCategoria()
            if categorias != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    categorias = ClientServiceCategoria.ongetClientServiceCategoriaName(search)
                    return render("client/ClientCategoriaView.html", categorias=categorias, tag = tag)
                else:
                    flash('Categorias Listadas', category='success')
                    return render("client/ClientCategoriaView.html", categorias=categorias)
            else:
                flash('No existe categorias', category='success')
                return render("client/ClientCategoriaView.html", categorias=categorias)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)