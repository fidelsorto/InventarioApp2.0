from flask import Flask, render_template, request, redirect, session
from routes.main import MainRoutes
from routes.dashboard import DashboardRoutes
from routes.log import LogRoutes

app = Flask(__name__)
app.secret_key = "Bad1secret2key3!+"


MainRoutes.configure_routes(app)
LogRoutes.configure_routes(app)


if __name__ == "__main__":
    app.run(debug=True)
