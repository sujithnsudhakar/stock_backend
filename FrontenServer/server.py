from flask import Flask, render_template, redirect, request, send_file
#import main

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    selectedCompany = ""
    if request.method == "POST":
        selectedCompany = request.form.get("comp")
        selectedDate = request.form.get("timeframe")
        print(selectedCompany)
        print(selectedDate)
    #company = main.get_stocknames()
    company = ["Apple", "Tesla"]
    return render_template('index.html', company=company)

