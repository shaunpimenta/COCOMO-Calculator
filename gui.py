from flaskwebgui import FlaskUI
from main import app
FlaskUI(app).close_server_on_exit
FlaskUI(app, width=1300, height=900,close_server_on_exit=False).run()
FlaskUI(app)