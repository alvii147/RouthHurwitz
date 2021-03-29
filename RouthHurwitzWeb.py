from flask import Flask, render_template, request
from RouthHurwitz import RouthHurwitz, ToLaTeX

app = Flask(__name__)
with open('secret_key.txt', 'r') as secret_key_file:
    app.secret_key = secret_key_file.read().strip()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        polynomial = request.form['polynomialInput']
        polynomial = polynomial.split(',')
        polynomial = [i.strip() for i in polynomial]
        return routharray(polynomial)
    return render_template('home.html')

def routharray(polynomial):
    routhArr = RouthHurwitz(polynomial)
    routhArr = ToLaTeX(routhArr)
    return render_template('routharray.html', routhArr = routhArr)

if __name__ == '__main__':
    app.run(debug = True)