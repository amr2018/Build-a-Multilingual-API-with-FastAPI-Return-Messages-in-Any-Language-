

from fastapi import FastAPI, Request
import json

app = FastAPI()

# load langs
langs = json.load(open('langs.json', 'r', encoding='utf-8'))


@app.get('/')
def index(request : Request):
    # get the languge from cookies
    lang = request.cookies.get('lang', 'en')
    return {'msg': langs[lang]['greet']}

