from flask import Flask, request, render_template
from parse_price import sku_to_price, sku, price

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
        



@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # sku = request.form['sku']
        # cost = sku(sku)
        return render_template('result.html', cost=20)


if __name__ == "__name__":
    app.run(ssl_context='adhoc')
