from os import getenv
from flask import Flask, render_template, request, url_for
import whois
from dotenv import load_dotenv

# Create a Flask application
app = Flask(__name__)

# Load environment variables from a .env file
load_dotenv()

# Set the secret key for the Flask application
app.secret_key = getenv("SECRET_KEY")

# Define a route for the index page, which handles both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    The main route for the application.
    Handles both GET and POST requests.
    """
    if request.method == 'POST':
        # If the request is a POST, extract the domain name from the form
        domain_name = request.form.get('domain_name')
        # Get WHOIS information for the provided domain name
        whois_info = grab_whois_info(domain_name)
        # Render the 'view.html' template with the domain name and WHOIS information
        return render_template('view.html', domain_name=domain_name, whois_info=whois_info)
    if request.method == 'GET':
        # If the request is a GET, render the 'index.html' template
        return render_template('index.html')

# Define a function to grab WHOIS information for a given domain name
def grab_whois_info(domain_name):
    """
    Retrieve WHOIS information for the provided domain name.
    """
    try:
        # Use the 'whois' library to get WHOIS information
        whois_info_result = whois.whois(domain_name)
        #print("Whois Info Result:", whois_info_result)
        return whois_info_result
    except whois.Exception as e:
        print("Exception:", e)
        # Handle exceptions and return an error message if WHOIS information cannot be retrieved
        return str(e)

# Run the Flask application if the script is executed
if __name__ == "__main__":
    app.run(debug=True)
