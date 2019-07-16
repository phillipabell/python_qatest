# Python HTTP services and Test Automation library

Creates a HTTP RESTful service and automates testing of that service.

## Installation

Clone the files to your local repository.

Requires Python 3.7

pip3 install -r requirements.txt   # To install third-party packages

## Usage

python restpkg/rest.py # To run the local HTTP server 

curl http://127.0.0.1:5000/us_state_codes/Colorado # returns 'words'
foobar.pluralize('goose') # returns {
    "us-state": "Colorado",
    "us-state-code": "CO"
}

pytest # runs all test cases

py.test test/test_GET_Colorado.tavern.yaml -v  # To test the Colorado endpoint

## License
[MIT](https://choosealicense.com/licenses/mit/)