from flask import Flask
import requests
import webbrowser

# https://media.merriam-webster.com/audio/prons/[language_code]/[country_code]/[format]/[subdirectory]/
# [base_filename].[format]
# these values will always be the same, language code: en, country code: us, format: mp3
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}"""
apiKey = "8ce9ae17-bab0-4ea9-bf32-a3441e69db3c"

app = Flask(__name__)


@app.get('/<query>')
def getFile(query):
    return receiveLink(query)


def getJson(word):
    api_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=" + apiKey
    response = requests.get(api_url)
    return response.json()


def receiveLink(word):
    subdirectory = word[0:1]
    for i in punctuation:
        if word[0:1] == i or word[:1].isdigit():
            subdirectory = "number"
    if word[0:2] == 'gg':
        subdirectory = 'gg'
    elif word[0:3] == 'bix':
        subdirectory = 'bix'
    base_filename = getJson(word)[0]["hwi"]['prs'][0]['sound']['audio']
    link = "https://media.merriam-webster.com/audio/prons/en/us/mp3/" + subdirectory + "/" + base_filename + ".mp3"
    webbrowser.open(link)

