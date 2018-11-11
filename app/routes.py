# coding=utf-8

from flask import render_template, flash, redirect, session, url_for, request, g, Markup
from app import app

@app.route('/')
@app.route('/index')
def index():
    apps = [
    {'appname':'simpleportfoliomc', 'label':'Simple portfolio MC simulator'},
    ]

    return render_template('index.html', apps=apps)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shiny/')
def shiny():
    # Get the app name from the template - the 'shinyapp' arg in 'url_for()'
    myvar = request.args.get('shinyapp', "")

    # Uses the value of 'myvar' to build the url for the Shiny app in 'shiny.html'
    return render_template('shiny.html', shinyapp=myvar)
