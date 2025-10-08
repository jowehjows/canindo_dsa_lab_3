from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/myworks')
def myworks():
    return render_template('myworks.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == "POST":
        try:
            radius = float(request.form.get("radius", 0))
            result = 3.14159 * radius * radius
        except ValueError:
            result = "Invalid input"
    return render_template("circle.html", result=result)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == "POST":
        try:
            base = float(request.form.get("base", 0))
            height = float(request.form.get("height", 0))
            result = 0.5 * base * height
        except ValueError:
            result = "Invalid input"
    return render_template("triangle.html", result=result)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
