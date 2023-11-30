from flask import render_template as render, request
from src.admin.services.adminServiceUsers import AdminServiceUser
from sqlalchemy.exc import SQLAlchemyError
import numpy
class AdminControllerUser:

    def onGetAdminControllerUserList():

        try:
            users = AdminServiceUser.ongetAdminServiceUser()
            if users is not None:
                return render("admin/adminUsers.html", users = users)
            else:
                return render("admin/adminUsers.html", users = users)
        except SQLAlchemyError as e:
                print("Error en Service User ", e)
                return render('errors/error500.html')    
        #else:
            #return render('errors/error401.html')