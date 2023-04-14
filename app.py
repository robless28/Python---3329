from flask import Flask, render_template, request

app = Flask(__name__)


# Function to read details for page 
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f] 
    
def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)


@app.route('/')
def homePage():
    name = "My Page"
    details = readDetails('static/details.txt')
    return render_template('homepage.html', name = name, aboutMe = details)
# flask run    # python app.py


################################

# def greet(name):
@app.route('/user/<name>')
def greet(name):
    return f'<p>Hello, {name}!</p>'

@app.route('/slay', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        # name = request.form['name']
        if request.form['message']:
            writeToFile('/static/comments.txt', request.form['messgae'])

    return render_template('form.html', name=name)

## When running this file directtly...
if __name__ == '__main__':
    app.run(debug=True)