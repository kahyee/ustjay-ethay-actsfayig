import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup
import json

app = Flask(__name__)


template = """https://github.com/kahyee/ustjay-ethay-actsfayig.git"""


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact().strip()
    payload = {"input_text": fact}
    
    
    r = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/", data = payload, allow_redirects=False)
    url = r.headers['Location']
    link = "<a href=" + "\"" + url+ "\"> click here </a>"
    print(link)
    
    
    return Response(response = link, mimetype="text")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

