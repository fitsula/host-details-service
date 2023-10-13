from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_hostname():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
        Server hostname: <b>{socket.gethostname()}</b><br>
        Current Date and Time: <b>{current_time}</b>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

