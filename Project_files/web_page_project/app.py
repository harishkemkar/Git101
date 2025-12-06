from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Instead of returning raw HTML, render the template
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(debug=True)