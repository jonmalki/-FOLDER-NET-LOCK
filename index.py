import qrcode
import subprocess
import socket
from flask import Flask, render_template_string, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Folder Lock</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        h1 {
            font-size: 24px;
            margin: 0 0 20px;
            color: #007aff;
        }
        #status {
            font-size: 18px;
            margin: 0 0 20px;
        }
        button {
            font-size: 18px;
            padding: 10px 20px;
            margin: 0 0 10px;
            background-color: #007aff;
            border: none;
            border-radius: 5px;
            color: #fff;
            cursor: pointer;
        }
        button:hover {
            background-color: #006ae6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Folder Lock</h1>
        <p id="status">{{ status }}</p>
        <form action="/lock" method="get">
            <button type="submit">Lock</button>
        </form>
        <form action="/unlock" method="get">
            <button type="submit">Unlock</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Get the status of the folder
    status = 'Unlocked' if os.path.exists('f0ld3r') else 'Locked'
    # Render the web page with the status message and buttons
    return render_template_string(html, status=status)

@app.route('/lock')
def lock_folder():
    # Lock the folder
    subprocess.run(["chflags", "hidden", "f0ld3r"])
    return redirect(url_for('index'))

@app.route('/unlock')
def unlock_folder():
    # Unlock the folder
    subprocess.run(["chflags", "nohidden", "f0ld3r"])
    return redirect(url_for('index'))

# Get the local IP address of the Mac
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Run the Flask application on port 5001
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# Delete the QR code images from disk after the script stops running
os.remove('static/lock_qr.png')
os.remove('static/unlock_qr.png')
