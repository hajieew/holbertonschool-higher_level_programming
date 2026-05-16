from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    products = []
    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


@app.route('/products')
def products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []
    error = None

    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    else:
        return render_template("product_display.html", error="Wrong source", products=[])

    if product_id:
        try:
            product_id = int(product_id)
        except:
            return render_template("product_display.html", error="Product not found", products=[])

        filtered = [p for p in data if int(p["id"]) == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])

        data = filtered

    return render_template("product_display.html", products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)