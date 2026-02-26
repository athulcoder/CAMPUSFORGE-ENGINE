from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


migrate = Migrate()
jwt = JWTManager()