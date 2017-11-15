from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static' ### Add static folder (css style)

@app.route("/")
def indexPage():
    return render_template('index.html')

@app.route("/add_device")
def formDevicePage():
    return render_template('add_device.html')

@app.route("/add_model")
def formModelPage():
    return render_template('add_model.html')

@app.route("/list_device")
def listDevicePage():
    return render_template('list_device.html')

@app.route("/list_model")
def listModelPage():
    return render_template('list_device.html')

if __name__ == "__main__":
    app.run()
