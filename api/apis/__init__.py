# apis/__init__.py
from flask import Flask
from apis.db import db
from apis.main.routes import main_bp
from apis.personal.routes import personal_bp

def thomas_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(personal_bp)

    return app
