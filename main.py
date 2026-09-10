from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_moeda', methods=['POST'])
def converter_moeda():
    reais = float(request.form['reais'])

    if reais <=0 :
        dolares = 'Nao pode'
    else:

        dolares = round((reais / 5.0979001),2)

    return render_template('index.html', reais=reais, dolares=dolares)
if __name__ == '__main__':
    app.run(debug=True)