from flask import Flask, config
from ETLTools.main.routes import main
from ETLTools.admin.routes import admin

app = Flask(__name__)


app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
##app.config.from_object(config.DevelopmentConfig)