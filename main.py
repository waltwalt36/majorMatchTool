from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(port=54321, debug=True)
    