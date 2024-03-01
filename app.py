from flask import Flask
#__name__ == "__main__"
app = Flask(__name__)

@app.route("/about") #definição de rota padrão, wuando está no link  http://localhost:5000/about
def about():
    return "Página Sobre"

def hello_world():
    return "Hello world!"

if __name__ == '__main__': 
    app.run(debug=True)  #inicia o servidor em modo debug 