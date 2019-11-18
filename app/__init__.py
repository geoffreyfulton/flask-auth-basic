from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_user import login_required, UserManager 
from config import DevConfig
from app.models import User

def create_app(config_class=DevConfig):
    """ Flask app factory """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)

    with app.app_context():
        from app.models import db
        db.init_app(app)

        # Setup Flask-User and specify the User data-model
        user_manager = UserManager(app, db, User)


        @app.route('/')
        def index():
            return render_template('index.html')

        
        @app.route('/members')
        @login_required
        def members():
            return render_template('members.html')

    
    return app



    
