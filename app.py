from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/product/<int:product_id>")
def product_page(product_id):
    return render_template('product-page.html', product_id=product_id)

if __name__ == '__main__':
    app.run(port=5000)

#    59  gcloud compute forwarding-rules list
#    60  sudo apt install authbind
#    61  sudo touch /etc/authbind/byport/80
#    62  sudo chmod 777 /etc/authbind/byport/80
#    63  authbind --deep python3 app.py