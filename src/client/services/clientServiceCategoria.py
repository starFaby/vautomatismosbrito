from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class ClientServiceCategoria:
    
    @classmethod
    def ongetClientServiceCategoria(self):
        try:
            categoriaList = Categoria.query.filter(Categoria.pfsabcateestado == 1)
            return categoriaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def ongetClientServiceCategoriaName(self, search):
        try:
            categoriaList = Categoria.query.filter(Categoria.pfsabcatenombre.like(search)).filter(Categoria.pfsabcateestado == 1)
            return categoriaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)