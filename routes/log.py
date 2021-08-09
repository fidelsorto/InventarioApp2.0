from flask import request, render_template, redirect, session, flash
from logic.admin_logic import AdminLogic
from logic.product_logic import ProdLogic
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
                Alogic = AdminLogic()
                adminDict =  Alogic.getValidateAdmin(user, passwd)

                if adminDict == []:
                    return render_template("login.html")
                else:
                     return render_template("crud.html")

        @app.route("/insert", methods=["GET", "POST"])
        def insert():
            if request.method == "GET":
                return render_template("crud.html")
            elif request.method == "POST":
                sku = request.form["sku"]
                name = request.form["name"]
                quantity = request.form["quantity"]
                price = request.form["price"]
                size = request.form["size"]
                color = request.form["color"]
                category = request.form["category"]
                photo = None

                Plogic = ProdLogic()
                rows = Plogic.insertProduct(sku, name, quantity, price, size, color, category, photo)

                if rows > 0:
                    return render_template("login.html")
                else:
                     return render_template("crud.html")

