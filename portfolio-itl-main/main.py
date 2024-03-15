# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Esecuzione della pagina dei contenuti
@app.route('/')
def index():
    return render_template('index.html')


# Competenze dinamiche
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)
