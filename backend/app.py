# Import Flask class to create a web application
# Import jsonify to return JSON responses
from flask import Flask, jsonify


# This function creates and configures the Flask app
# We use a factory function so the app can scale later
def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Define a route (API endpoint)
    # This endpoint is used to check if the app is running
    @app.route("/health", methods=["GET"])
    def health_check():
        # Return a JSON response indicating the app is healthy
        return jsonify({
            "status": "OK",
            "message": "AI Integration Automation Platform is running"
        })

    # Return the configured app object
    return app


# This block ensures the app runs only when this file
# is executed directly (not when imported elsewhere)
if __name__ == "__main__":
    # Create the Flask app
    app = create_app()

    # Start the development server
    # debug=True enables auto-reload and better error messages
    app.run(debug=True)
