# Import Flask class to create the web application
from flask import Flask, jsonify

# Import requests library to call external APIs manually
import requests


def create_app():
    """
    This function creates and configures the Flask application.
    Using a factory function is a best practice for scalability.
    """
    
    # Create a Flask app instance
    app = Flask(__name__)

    # -------------------------------
    # HEALTH CHECK ENDPOINT
    # -------------------------------
    @app.route("/health", methods=["GET"])
    def health_check():
        """
        This endpoint is used to check if the backend service is running.
        It is commonly used by monitoring tools.
        """
        return jsonify({
            "status": "OK",
            "message": "AI Integration Automation Platform is running"
        })

    # -------------------------------
    # MANUAL EXTERNAL API INTEGRATION
    # -------------------------------
    @app.route("/external-post", methods=["GET"])
    def get_external_post():
        """
        This endpoint manually calls an external public API.
        This demonstrates real backend integration skills.
        """

        # URL of the external API (public, no authentication required)
        external_api_url = "https://jsonplaceholder.typicode.com/posts/1"

        try:
            # Send GET request to the external API
            response = requests.get(
                external_api_url,
                timeout=5  # Prevents hanging if API is slow/unavailable
            )

            # Raise exception if HTTP status code is 4xx or 5xx
            response.raise_for_status()

            # Convert JSON response into Python dictionary
            data = response.json()

            # Return structured response to the client
            return jsonify({
                "source": "jsonplaceholder",
                "success": True,
                "data": data
            })

        except requests.exceptions.Timeout:
            # Handles API timeout error
            return jsonify({
                "success": False,
                "error": "External API request timed out"
            }), 504

        except requests.exceptions.RequestException as e:
            # Handles all other request-related errors
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500

    # Return the configured Flask app
    return app

    @app.route("/")
    def home():
        return "Backend is running"

# -------------------------------
# APPLICATION ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    # Create the Flask app using the factory function
    app = create_app()
    print(app.url_map)
    # Run the Flask development server
    app.run(debug=True)
