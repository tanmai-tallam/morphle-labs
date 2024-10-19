from flask import Flask
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Tanmai Tallam"

    username = getpass.getuser()

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    try:
        top_output = subprocess.getoutput('top -b -n 1')
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

    result = f"""
    Name: {name}<br>
    Username: {username}<br>
    Server Time (IST): {server_time}<br><br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """
    
    return result

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)