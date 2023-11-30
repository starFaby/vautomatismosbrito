from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.admin.model.adminModelCategoria import ModelCategoria
import datetime

class AdminServiceCategoria:

    @classmethod
    def onGetAdminServiceCategoriaAll(self):
        try:
            categoriaList = Categoria.query.all()
            return categoriaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    @classmethod
    def ongetAdminServiceCategoria(self, page):
        try:
            page = page
            pages = 10
            categoriaList = Categoria.query.order_by(Categoria.pfsabcateid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return categoriaList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def ongetAdminServiceCategoriaName(self, search, page):
        try:
            page = page
            pages = 10
            categoriaList = Categoria.query.filter(Categoria.pfsabcatenombre.like(search)).paginate(per_page=pages,error_out=False)
            return categoriaList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')

    @classmethod    
    def onGetAdminServiceCategoriaSave(self, pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat):
        try:
            modelCategoria = ModelCategoria(0,pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat)
            newCategoria = Categoria(pfsabcatenombre = modelCategoria.getpfsabcatenombre(), pfsabcateimage=modelCategoria.getpfsabcateimage(), pfsabcatedetalle = modelCategoria.getpfsabcatedetalle(), pfsabcateestado = modelCategoria.getpfsabcateestado(), pfsabcatecreatedat = modelCategoria.getpfsabcatecreatedat())
            db.session.add(newCategoria)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceCategoriaUpdateSelect(self, id):
        try:
            categoria = Categoria.query.get(id)
            return categoria
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceCategoriaUpdate(self, id, pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat):
        try:
            categoria = Categoria.query.get(id)
            modelCategoria =  ModelCategoria(0, pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat)
            categoria.pfsabcatenombre = modelCategoria.getpfsabcatenombre()
            categoria.pfsabcateimage = modelCategoria.getpfsabcateimage()
            categoria.pfsabcatedetalle = modelCategoria.getpfsabcatedetalle()
            categoria.pfsabcateestado = modelCategoria.getpfsabcateestado()
            if categoria.pfsabcatenombre != '' and categoria.pfsabcateimage != '' and categoria.pfsabcatedetalle != '' and categoria.pfsabcateestado != 'Elija...':
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceCategoriaDelete(self, id , pfsabcateestado):
        pfsabcatenombre = ''
        pfsabcateimage = ''
        pfsabcatedetalle = ''
        pfsabcatecreatedat = ''
        categoria = Categoria.query.get(id)
        if categoria.pfsabcateid >= 1: 
            modelCategoria = ModelCategoria(id, pfsabcatenombre, pfsabcateimage, pfsabcatedetalle, pfsabcateestado, pfsabcatecreatedat)
            categoria.pfsabcateestado = modelCategoria.getpfsabcateestado()
            db.session.commit()
            return True
        else:
            return False