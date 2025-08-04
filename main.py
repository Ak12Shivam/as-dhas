from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configure the template folder to the current directory
app.template_folder = '.'

@app.route('/')
def index():
    """Serve the main landing page"""
    return render_template('s.html')

@app.route('/favicon.ico')
def favicon():
    """Handle favicon requests"""
    return send_from_directory(os.path.join(app.root_path, '.'), 
                             'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('s.html'), 404

if __name__ == '__main__':
    print("🚀 Starting AI/ML Workshop Landing Page Server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    
    # Run the Flask development server
    app.run(
        host='0.0.0.0',  # Allow access from other devices on the network
        port=5000,       # Port number
        debug=True,      # Enable debug mode for development
        threaded=True    # Handle multiple requests simultaneously
    )
