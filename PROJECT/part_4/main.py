# CSE115LLRA Computer Science I:220110202
# Project 1: Module 4
# Made by Hardik Goel
# Date Started: April 22, 2020
# Module 4 due date: May 1, 2020

import bottle
import json
import cache
import backend

@bottle.route('/')
def load_html():
    return bottle.static_file("index.html", root="client/")

@bottle.route('/ajax.js')
def load_ajax():
    print("Retrieveing AJAX File")
    return bottle.static_file("ajax.js", root="client/")

@bottle.route('/script.js')
def load_js():
    print("Retrieveing SCRIPT File")
    return bottle.static_file("script.js", root="client/")

@bottle.route('/scatter_plot')
# tows on each day of the month
def tows_data():
    raise NotImplementedError

@bottle.route('/pie_chart')
# police districts were responsible for tows
def district_data():
    raise NotImplementedError

@bottle.route('/line_plot')
# cars were towed and how those reasons change
def tow_description():
    raise NotImplementedError