from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

def get_state_options(counties):
    states= []
    options=""
    '''for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + s + "\">" + s + "</option>")'''
    return options

if __name__=="__main__":
    app.run(debug=False, port=54321)
