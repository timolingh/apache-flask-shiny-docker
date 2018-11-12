# coding=utf-8

from flask import render_template, flash, redirect, session, url_for, request, g, Markup
from app import app

@app.route('/')
@app.route('/index')
def index():

    EC2ADDRESS = '10.0.0.150'

    DASHBOARDAPPS = [
    {'appname':'dashboard_app',         'label':'Jemstep AUM'},
    {'appname':'event_stream',          'label':'Platform user events'},
    {'appname':'engineering_delivery',  'label':'Code delivery metrics'}
    ]

    SHINYAPPS = [
    {'appname':'montecarloreturns',     'label':'Simple portfolio MC simulator'},
    ]

    return render_template('index.html',
                           ec2address=EC2ADDRESS,
                           dashboardapps=DASHBOARDAPPS,
                           shinyapps = SHINYAPPS
                           )

@app.route('/about')
def about():
    return render_template('about.html')

## Not currently used
@app.route('/shiny/')
def shiny():
    # Get the app name from the template - the 'shinyapp' arg in 'url_for()'
    myvar = request.args.get('shinyapp', "")

    # Uses the value of 'myvar' to build the url for the Shiny app in 'shiny.html'
    return render_template('shiny.html', shinyapp=myvar)
