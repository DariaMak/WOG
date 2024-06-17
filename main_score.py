from utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask, render_template

def score_server():
    app = Flask(__name__)

    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()

        @app.route('/')
        def show_score():
            return render_template('score.html', score=score)

    except FileNotFoundError:
        @app.route('/')
        def show_error():
            error_message = "Something went wrong! File not found!"
            return render_template('error.html', error=error_message)

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)

score_server()
