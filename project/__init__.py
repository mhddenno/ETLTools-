from flask import Flask
from project.main.routes import main
from project.admin.routes import admin

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')