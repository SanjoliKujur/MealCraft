from flask import Flask, render_template, request, jsonify
from logic import match_recipes, df

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    ingredients = request.json.get("ingredients", "")
    return jsonify(match_recipes(ingredients, df) )

if __name__ == "__main__":
    app.run(debug=True)