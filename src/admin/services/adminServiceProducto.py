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
    def onGetAdminServiceConsultUpdate(self, id, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid):
        try:
            consulta = Consulta.query.get(id)
            modelConsulta =  ModelConsulta(0, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage,
                                            pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat,
                                            pfspcrcateid)
            consulta.pfspcrconsultseccion = modelConsulta.getpfspcrconsultseccion()
            consulta.pfspcrconsultnum = modelConsulta.getpfspcrconsultnum()
            consulta.pfspcrconsultnombre = modelConsulta.getpfspcrconsultnombre()
            consulta.pfspcrconsultimage = modelConsulta.getpfspcrconsultimage()
            consulta.pfspcrconsultdetalle = modelConsulta.getpfspcrconsultdetalle()
            consulta.pfspcrconsulturl = modelConsulta.getpfspcrconsulturl()
            consulta.pfspcrconsultestado = modelConsulta.getpfspcrconsultestado()
            consulta.pfspcrcateid = modelConsulta.getpfspcrcateid()
            db.session.commit()

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceConsultaDelete(self, id , pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid):
        
        consulta = Consulta.query.get(id)
        if consulta.pfspcrconsultid >= 1:
            modelConsulta = ModelConsulta(id, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid)
            consulta.pfspcrconsultestado = modelConsulta.getpfspcrconsultestado()
            db.session.commit()
            return True
        else:
            return False