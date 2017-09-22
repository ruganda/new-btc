
from app import app
from flask import current_app
if __name__== '__main__':
    with app.app_context():
        app.run()