# Spell Tester
The microservice will take the inputted word and in return provide an mp3 with the pronunciation of the word. 
An example for the word pajama would be https://media.merriam-webster.com/audio/prons/en/us/mp3/p/pajama02.mp3
The link is broken down into the following form 
https://media.merriam-webster.com/audio/prons/[language_code]/[country_code]/[format]/[subdirectory]/[filename].[format].
The language code, country code, and format will all be default values and be the same regardless of the inputted word. 
The subdirectory and filename depend on the inputted word. Speficially the filename will be found in the requested json file. 


# Requesting Data
The user can request data by calling the receieveLink function and passing their desired word as a parameter. 
The function will call the getJson function which requests a json file from Merriam-Webster using the link https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}key={apiKey}

# Receiving Data
After requesting the json file throug hthe Merriam-Webster API, a json file will be provided. 
```yaml

{
  "hw":"pa*ja*ma",
  "prs":[
    {
      "mw":"p\u0259-\u02c8j\u00e4-m\u0259",
      "sound":{
        "audio":"pajama02",
        "ref":"c",
        "stat":"1"
      }
    },{
      "mw":"-\u02c8ja-",
      "sound":{
        "audio":"pajama01",
        "ref":"c",
        "stat":"1"
      }
    }
  ]
}
    
```
Within the json file the "audio" key will be the base filename in the mp3 link. 

