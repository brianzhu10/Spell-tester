import json

# https://media.merriam-webster.com/audio/prons/[language_code]/[country_code]/[format]/[subdirectory]/[base filename].[format]
# these values will always be the same, language code: en, country code: us, format: mp3
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}"""

word = 'voluminious'
subdirectory = ''
for i in punctuation:
    if word[0:1] == i or word[:1].isdigit():
        subdirectory = "number"
if word[0:2] == 'gg':
    subdirectory = 'gg'
elif word[0:3] == 'bix':
    subdirectory = 'bix'
else:
    subdirectory = word[0:1]

f = open('voluminous.json')
data = json.load(f)
filename = data['prs']['sound']['audio']
f.close()

link = "https://media.merriam-webster.com/audio/prons/en/us/mp3/" + subdirectory + "/" + filename + ".mp3"
print(link)