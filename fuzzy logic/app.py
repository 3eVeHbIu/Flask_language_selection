from flask import Flask, render_template, request

import skfuzzy 

import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title='Форма')


@app.route('/answer', methods=['POST'])
def show_answer():
    pass

if __name__ == '__main__':
    app.run(debug=True)
