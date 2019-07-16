from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

us_state_codes =  [
    {
    "us-state": "Colorado",
    "us-state-code": "CO"
    },
    {
    "us-state": "Florida",
    "us-state-code": "FL"
    },
    {
    "us-state": "New York",
    "us-state-code": "NY"
    }
]

class US_State_Codes(Resource):

    def get(self, name):
        for us_state in us_state_codes:
           if (name == us_state["us-state"]):
               return us_state, 200
        return "No US state found", 404

api.add_resource(US_State_Codes, "/us_state_codes/<string:name>")

@app.route('/')
def index():
    html = "US State Codes<p>"
    html += "<a href='/us_state_codes/Colorado'>Colorado</a><br>"
    html += "<a href='/us_state_codes/Florida'>Florida</a><br>"
    html += "<a href='/us_state_codes/New York'>New York</a><br>"
    return html

app.run(debug=True)