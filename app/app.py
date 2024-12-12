from flask import Flask
from routes.user_routes import user_blueprint
from routes.destinations_routes import destinations_blueprint
from routes.package_routes import package_blueprint
from routes.booking_routes import booking_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user_blueprint, url_prefix="/api/users")
app.register_blueprint(destinations_blueprint, url_prefix="/api/destinations")
app.register_blueprint(package_blueprint, url_prefix="/api/packages")
app.register_blueprint(booking_blueprint, url_prefix="/api/bookings")

if __name__ == "__main__":
    app.run(debug=True)
