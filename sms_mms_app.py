from flask import Flask, request, redirect
from twilio import twiml
import requests 
import json

app = Flask(__name__)

my_number  = '+'
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    response = requests.get("https://favqs.com/api/qotd", timeout = 15)
    data = json.loads(response.content)           
    daily_quote = data['quote']['body'] 

    response_image = requests.get('https://api.thecatapi.com/v1/images/search')
    data_image = json.loads(response_image.content)
    image_url = data_image[0]['url']


    body = request.values.get('Body', None)
    # from_number = request.values.get('From', None)
    # if from_number == my_number:

    if body == 'Yes' or body == 'yes':
        return """<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Message>
                <Body>""" + daily_quote + """</Body>
                <Media>""" + image_url + """ </Media>
            </Message>
        </Response>"""
    elif body == "No":
        return """<?xml version="1.0" encoding="UTF-8"?><Response><Sms> Hello, you have said No!</Sms></Response>"""
    else: 
        return """<?xml version="1.0" encoding="UTF-8"?><Response><Sms>Please say Yes or No</Sms></Response>"""


if __name__ == "__main__":
    app.run(debug=True)