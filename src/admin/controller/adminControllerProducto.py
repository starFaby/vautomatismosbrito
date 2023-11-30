from flask import render_template as render, request, flash, redirect, url_for
from src.admin.services.adminServiceProducto import AdminServiceProducto
from src.admin.services.adminServiceCategoria import AdminServiceCategoria
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime


class AdminControllerProducto:

    def onGetAdminControllerProductoList(page):
        try:
            page = page
            producto = AdminServiceProducto.ongetAdminServiceProducto(page)
            categorias = AdminServiceCategoria.onGetAdminServiceCategoriaAll()
            if producto != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    producto = AdminServiceProducto.ongetAdminServiceProductoName(search, page)
                    return render("admin/adminProducto.html",categorias = categorias, producto=producto, tag = tag)
                else:
                    flash('Consultas Listadas', category='success')
                    return render("admin/adminProducto.html",categorias = categorias, producto=producto)
            else:
                flash('No existe consultas', category='success')
                return render("admin/adminProducto.html",categorias=categorias, producto=producto)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    def onGetControllerAdminProductoSave():

        pfsabprodnombre = request.form['txtNombre']
        pfsabprodimage = request.form['txtImage']
        pfsabproddetalle = request.form['txtDetalle']
        pfsabprodprecio = request.form['txtPrecio']
        pfsabprodstock = request.form['txtStock']
        pfsabprodestado = request.form['selectEstado']
        pfsabprodcreatedat = datetime.now()
        pfsabcategoriaid = request.form['selectCategoria']

        if  pfsabprodnombre != '' and pfsabprodimage != '' and pfsabproddetalle != '' and pfsabprodprecio != '' and pfsabprodstock != '' and pfsabprodestado != 'Elija...' and pfsabprodcreatedat != '' and pfsabcategoriaid != '' :
            AdminServiceProducto.onGetAdminServiceProductoSave(pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid)
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('arp.onGetAdminControllerProductoList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            print("Datos vacios")
            return redirect(url_for('arp.onGetAdminControllerProductoList'))          

    def onGetControllerAdminProductoUpdate(id):
        producto = AdminServiceProducto.onGetAdminServiceProductoUpdateSelect(id)
        categorias = AdminServiceCategoria.onGetAdminServiceCategoriaAll()
        if request.method == 'POST':
            pfsabprodnombre = request.form['txtNombre']
            pfsabprodimage = request.form['txtImage']
            pfsabproddetalle = request.form['txtDetalle']
            pfsabprodprecio = request.form['txtPrecio']
            pfsabprodstock = request.form['txtStock']
            pfsabprodestado = request.form['selectEstado']
            pfsabprodcreatedat = datetime.now()
            pfsabcategoriaid = request.form['selectCategoria']
            if pfsabprodnombre != '' and pfsabprodimage != '' and pfsabproddetalle != '' and pfsabprodprecio != '' and pfsabprodstock != '' and pfsabprodestado != 'Elija...' and pfsabprodcreatedat != '' and pfsabcategoriaid != '' :
                adServConsult = AdminServiceProducto.onGetAdminServiceProductUpdate(id, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid)
                if adServConsult == True:
                    flash('Datos Actualizados', category='success')
                    return redirect(url_for('arp.onGetAdminControllerProductoList'))
                else:
                    flash('Campos vacios llene porfabor', category='success')
                    return redirect(url_for('arp.onGetAdminControllerProductoList'))
            else:
                    flash('Campos vacios llene porfabor', category='success')
                    return redirect(url_for('arp.onGetAdminControllerProductoList'))

        return render("modal/modalAdminProductoUpdate.html", producto = producto, categorias = categorias)   

    def onGetControllerAdminProductoDelete(id):
        pfsabprodnombre = ''
        pfsabprodimage = ''
        pfsabproddetalle = ''
        pfsabprodprecio = ''
        pfsabprodstock = ''
        pfsabprodestado = 0
        pfsabprodcreatedat = ''
        pfsabcategoriaid = ''
        if  pfsabprodnombre == '' and pfsabprodimage == '' and pfsabproddetalle == '' and pfsabprodprecio == '' and pfsabprodstock == '' and pfsabprodestado != '' and pfsabprodcreatedat == '' and pfsabcategoriaid == '' :
            producto = AdminServiceProducto.onGetAdminServiceProductoDelete(id, pfsabprodnombre, pfsabprodimage, pfsabproddetalle, pfsabprodprecio, pfsabprodstock, pfsabprodestado, pfsabprodcreatedat, pfsabcategoriaid)     
            if producto == True:
                flash('Datos Actualizados', category='success')
                return redirect(url_for('arp.onGetAdminControllerProductoList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('arp.onGetAdminControllerProductoList'))
        else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('arp.onGetAdminControllerProductoList'))