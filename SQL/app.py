from flask import Flask
from sql_utils import execute_sql


app = Flask(__name__)

@app.route("/")
def products():
    query = "SELECT * FROM products;"
    data = execute_sql('exercises_db', query)
    list_products = []
    for product in data:
        list_products.append(product)
    return list_products

if __name__ == "__main__":
    app.run(debug=True, port=8000)