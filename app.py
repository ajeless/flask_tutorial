from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/product/<int:product_id>")
def product_page(product_id):
    return render_template('product-page.html', product_id=product_id)

if __name__ == '__main__':
    app.run(port=5000)