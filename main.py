from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from googlesearch import search


# chatbot logic
app = Flask(__name__)


@app.route("/", methods=["POST"])
def bot():

    # user input
    user_msg = request.values.get('Body', '').lower()

    # creating object of MessagingResponse
    response = MessagingResponse()

    # user query
    q = user_msg + "geeksforgeeks.org"

    # list to store urls
    results = []

    # searching and storing urls
    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        results.append(i)

    # displaying result
    msg = response.message(f"--- Results for '{user_msg}' --- ")
    for result in results:
        msg = response.message(result)

    return str(response)


if __name__ == "__main__":
    app.run()
