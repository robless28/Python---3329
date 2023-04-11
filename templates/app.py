from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('homepage.html')
# flask run    # python app.py

@app.route("/rockets")
def anotherPage():
    return "<p> This is another page </p> <a href='google.com'> Link to another site </a>"

# Function to read details for page 
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

################################

# def greet(name):
@app.route('/user/<name>')
def greet(name):
    return f'<p>Hello, {name}!</p>'

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        # if request.form['message']:
            # writeToFile('/static/comments.txt', request.form['messgae'])

    return render_template('form.html', name=name)

## When running this file directtly...
if __name__ == "__main__":
    app.run(debug=True, port=2000)