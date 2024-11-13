from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fahrenheit = None
    if request.method == 'POST':
        celsius = float(request.form['celsius'])
        fahrenheit = (celsius * 9/5) + 32
    return render_template('index.html', fahrenheit=fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)
