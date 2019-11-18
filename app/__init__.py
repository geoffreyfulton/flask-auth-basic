from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_user import login_required, UserManager, UserMixin
from config import DevConfig

def create_app(config_class=DevConfig):
    """ Flask app factory """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)

    with app.app_context():
        db = MongoEngine(app)

        # Define the User document.
        # NB: Make sure to add flask_user UserMixin !!!
        class User(db.Document, UserMixin):
            active = db.BooleanField(default=True)

            # User authentication information
            username = db.StringField(default='')
            password = db.StringField()

            # User information
            first_name = db.StringField(default='')
            last_name = db.StringField(default='')

            # Relationships
            roles = db.ListField(db.StringField(), default=[])        

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



    
