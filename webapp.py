from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
#allStates=""

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        return render_template('index.html', options = get_state_options(counties))
    #return render_template('index.html')

'''def get_state_options(counties):
    states= []
    options=""
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            #state_name and fun_fact
            state=c["State"]#state_counties(counties, c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + state + "</option>")
    #allStates = states 
    return options

def state_counties(counties, state):
    """Return the state with the average number of percent under of 18"""
    count=0
    i=0
    for c in counties:
        if state == c["State"]:
            i+=c["Percent Under 18 Years"]
            count+=1
    return i/count'''

if __name__=="__main__":
    app.run(debug=False, port=54321)
