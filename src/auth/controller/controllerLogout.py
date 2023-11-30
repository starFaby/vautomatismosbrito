# Salir por primera vez
from flask import flash, render_template as render
from flask_login import login_user, logout_user, login_required

class ControllerLogout:
        
    def onGetControllerLogout():
        logout_user()
        flash("Cerraste sesion !!", category="info")
        
        return render('index.html')