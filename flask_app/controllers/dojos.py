from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.survey import Dojo



@app.route('/')
def index():


    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():

    # if Dojo.validate_dojo(request.form):
    #     Dojo.save(request.form)
    #     return redirect('/result')
    # return redirect('/')
    if not Dojo.validate_dojo(request.form):
    
        return redirect('/')
    Dojo.save(request.form)
    return redirect('/result')

@app.route('/result')
def result():

    return render_template("result.html", dojo= Dojo.get_one())