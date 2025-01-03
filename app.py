from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Assignment</title>
        </head>
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f8ff;">
            <h1 style="color: #0000FF; font-family: Arial, sans-serif; text-align: center;">
                Hello, JITTAK! Welcome to the DevOps Assignment! By MUHAMMED ATHIF A L
            </h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
