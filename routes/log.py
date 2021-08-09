from flask import request, render_template, redirect, session, flash
from logic.admin_logic import AdminLogic

class LogRoutes():
    @staticmethod
    def configure_routes(app):

        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "GET":
                return render_template("login.html")
            elif request.method == "POST":
                user = request.form["user"]
                passwd = request.form["passwd"]
                logic = AdminLogic()
                adminDict =  logic.getValidateAdmin(user, passwd)

                if adminDict == []:
                    return render_template("login.html")
                else:
                     return render_template("crud.html")
