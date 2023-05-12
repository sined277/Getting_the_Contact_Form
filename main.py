from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def recive_data():
    # Get the values submitted from the login form
    name = request.form['username']
    password = request.form['password']
    
    # Display the name and password values in an HTML heading
    return f"<h1>Name: {name}, Password: {password}</h1>"

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
