from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.admin.model.adminModelProducto import ModelProducto
import datetime

class AdminServiceProducto:
    
    @classmethod
    def ongetAdminServiceProducto(self, page):
        try:
            page = page
            pages = 10
            productoList = Producto.query.order_by(Producto.pfsabprodid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return productoList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def ongetAdminServiceProductoName(self, search, page):
        try:
            page = page
            pages = 10
            productoList = Producto.query.filter(Producto.pfsabprodnombre.like(search)).paginate(per_page=pages,error_out=False)
            return productoList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)

    @classmethod    
    def onGetAdminServiceProductoSave(self, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid):
        try:
            modelProducto = ModelProducto(0, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid)
            
            newProducto = Producto( pfsabprodnombre = modelProducto.getpfsabprodnombre(), 
                                    pfsabprodimage = modelProducto.getpfsabprodimage(), 
                                    pfsabproddetalle = modelProducto.getpfsabproddetalle(), 
                                    pfsabprodprecio = modelProducto.getpfsabprodprecio(), 
                                    pfsabprodstock = modelProducto.getpfsabprodstock(), 
                                    pfsabprodestado = modelProducto.getpfsabprodestado(), 
                                    pfsabprodcreatedat = modelProducto.getpfsabprodcreatedat(),
                                    pfsabcategoriaid = modelProducto.getpfsabcategoriaid())
            db.session.add(newProducto)
            db.session.commit()

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceProductoUpdateSelect(self, id):
        try:
            producto = Producto.query.get(id)
            return producto
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceProductUpdate(self, id, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid):
        try:
            consulta = Producto.query.get(id)
            modelConsulta =  ModelProducto(0, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, 
                                        pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid)
            consulta.pfsabprodnombre = modelConsulta.getpfsabprodnombre()
            consulta.pfsabprodimage = modelConsulta.getpfsabprodimage()
            consulta.pfsabproddetalle = modelConsulta.getpfsabproddetalle()
            consulta.pfsabprodprecio = modelConsulta.getpfsabprodprecio()
            consulta.pfsabprodstock = modelConsulta.getpfsabprodstock()
            consulta.pfsabprodestado = modelConsulta.getpfsabprodestado()
            consulta.pfspcrconsultestado = modelConsulta.getpfsabprodestado()
            consulta.pfsabcategoriaid = modelConsulta.getpfsabcategoriaid()
            db.session.commit()

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceProductoDelete(self, id, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid):
        producto = Producto.query.get(id)
        if producto.pfsabprodid >= 1:
            modelProducto = ModelProducto(id, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid)
            producto.pfsabprodestado = modelProducto.getpfsabprodestado()
            db.session.commit()
            return True
        else:
            return False