from flask import Flask, request, render_template
from cdiscount_parser.price_parser import parse_price

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        sku = parse_price(request.form['sku'])
        return render_template('result.html', cost=sku)


if __name__ == "__name__":
    app.run(host='0.0.0.0',port=5000)
