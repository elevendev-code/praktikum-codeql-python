# vulnerable.py

import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd")
    os.system(cmd)  # ⚠️ Ini rentan terhadap command injection!
    return "Command executed"

if __name__ == "__main__":
    app.run()
