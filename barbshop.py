from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/produtos/')
def produtos():
   return render_template("Produtos.html")

@app.route('/contatos/')
def contatos():
   return render_template("Contatos.html")

if __name__ == '__main__':
   app.run(debug = False)

