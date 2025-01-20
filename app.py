from flask import Flask
from flasgger import Swagger
from mongodb_connection_manager import MongoConnectionHolder
from routes import initial_routes
import os

app = Flask(__name__)
Swagger(app)

# Initialize Database Connection
MongoConnectionHolder.initialize_db()

# Import the routes
initial_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8088))
    app.run(debug=True, port=port)