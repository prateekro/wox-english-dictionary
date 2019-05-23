# -*- coding: utf-8 -*-

from wox import Wox
import json
from pprint import pprint
import requests
# from oxford_dictionary_api import OxfordDictionaryAPI
import re
import isafe
import os
import pyperclip
from tinydb import TinyDB, Query
# import time

# from isafe import BASE_URL, LANGUAGE_CODE, entries, APP_ID, APP_KEY as cred


# from pprint import pprint
#
#
# pprint(data)

class PrateekDictionary(Wox):
    BASE_URL = isafe.CONFIG['BASE_URL'] 
    LANGUAGE_CODE = isafe.CONFIG['LANGUAGE_CODE'] 
    entries = isafe.CONFIG['entries'] 
    APP_ID = isafe.CONFIG['APP_ID'] 
    APP_KEY = isafe.CONFIG['APP_KEY']
    db = TinyDB('db.json')
    Word = Query()

    def copyText(self, textToCopy):
        # pyperclip.copy(textToCopy)
        """
        Copies the given value to the clipboard.
        WARNING: Uses yet-to-be-known Win32 API and ctypes black magic to work.
        """
        try:
            pyperclip.copy(textToCopy)
        except IOError:
            command = 'echo ' + textToCopy + '| clip'
            os.system(command)
        return None

    def resultOut(self, results, title = "{}".format("DEFAULT"), subtitle = "{}".format("DEFAULT"), IcoPath = "Images/app.ico", ContextData = "ctxData"):
        results.append({
            "Title": title,
            "SubTitle": subtitle,
            "IcoPath": IcoPath,
            "ContextData": ContextData,
            "JsonRPCAction": {
                'method': 'copyText',
                'parameters': ["{}".format(title)],
                'dontHideAfterAction': False
            }
        })

    def query(self, query):
        results = []
        if str(query).lower() == "intellij".lower():
            query = "Idea it is."

        self.resultOut(results, title = "Word: "+query, subtitle = "Word Length: {}".format(str(len(query))))

        suffix = "?"
        if query.endswith(suffix):
            # def meaning(self, word):
            # print("OxfordDictionaryAPI")
            query = query.split(".")[0]
            # query = self.BASE_URL + self.entries + self.LANGUAGE_CODE + query.lower()
            # getMeaning = requests()
            # getMeaning.status_code = 200
            # getMeaning.content = b'{ \n    "id": "confectioner", \n    "metadata": {\n        "operation": "retrieve",\n        "provider": "Oxford University Press",\n        "schema": "RetrieveEntry"\n    },\n    "results": [\n        {\n            "id": "confectioner",\n            "language": "en-us",\n            "lexicalEntries": [\n                {\n                    "entries": [\n                        {\n                            "senses": [\n                                {\n                                    "definitions": [\n                                        "a person whose occupation is making or selling candy and other sweets."\n                                    ],\n                                    "domains": [\n                                        {\n                                            "id": "sweet",\n                                            "text": "Sweet"\n                                        }\n                                    ],\n                                    "id": "m_en_gbus0209730.005",\n                                    "shortDefinitions": [\n                                        "person whose trade is making or selling confectionery"\n                                    ]\n                                }\n                            ]\n                        }\n                    ],\n                    "language": "en-us",\n                    "lexicalCategory": {\n                        "id": "noun",\n                        "text": "Noun"\n                    },\n                    "pronunciations": [\n                        {\n                            "audioFile": "http://audio.oxforddictionaries.com/en/mp3/xconfectioner_us_1.mp3",\n                            "dialects": [\n                                "American English"\n                            ],\n                            "phoneticNotation": "respell",\n                            "phoneticSpelling": "k\xc9\x99n\xcb\x88fekSH(\xc9\x99)n\xc9\x99r"\n                        },\n                        {\n                            "audioFile": "http://audio.oxforddictionaries.com/en/mp3/xconfectioner_us_1.mp3",\n                            "dialects": [\n                                "American English"\n                            ],\n                            "phoneticNotation": "IPA",\n                            "phoneticSpelling": "k\xc9\x99n\xcb\x88f\xc9\x9bk\xca\x83(\xc9\x99)n\xc9\x99r"\n                        }\n                    ],\n                    "text": "confectioner"\n                }\n            ],\n            "type": "headword",\n            "word": "confectioner"\n        }\n    ],\n    "word": "confectioner"\n		}'
            foundInLocal = self.db.all()
            foundInLocal = self.db.search(self.Word.word == '{}'.format(query))
            # foundInLocal = self.db.search(query == self.Word.word) #str(query.lower())
            self.resultOut(results, str(foundInLocal))
            if len(foundInLocal) > 0:
                # aT =
                # query = str(foundInLocal)
                wordX = foundInLocal[0]['word']
                definition = foundInLocal[0]['definition']
                DialectType = ""
                LexCategory = foundInLocal[0]['lex_category']
                PhoneticSpelling = foundInLocal[0]['phonetic_spelling']
                PhoneticDefinition = foundInLocal[0]['phonetic_definition']

                self.resultOut(results, "Definition: "+ foundInLocal[0]['word'] + " #[From Local]","{}: {} || {} || PhoneticDefinition: {}".format(DialectType, PhoneticSpelling, LexCategory, PhoneticDefinition))
                # self.db.insert({ "word" : wordX, "definition" : definition, "lex_category" : LexCategory , "phonetic_spelling": PhoneticSpelling, "phonetic_definition": PhoneticDefinition})
            else:
                self.resultOut(results, "SEND REQUEST")
                """
                getMeaning = requests.get(url = self.BASE_URL + self.entries + self.LANGUAGE_CODE + query.lower(), headers = {"app_id": self.APP_ID, "app_key": self.APP_KEY})
                if getMeaning.status_code == 200:
                    getMeaning = getMeaning.content
                    getMeaning = json.loads(getMeaning, encoding='utf-8')
                    #Definition
                    definition = str(getMeaning['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
                    query = definition
                    wordX = str(getMeaning['id'])
                    LexCategory = str(getMeaning['results'][0]["lexicalEntries"][0]["lexicalCategory"]["text"])
                    DialectType = str(getMeaning['results'][0]["lexicalEntries"][0]["pronunciations"][0]["dialects"][0])
                    PhoneticDefinition = str(getMeaning['results'][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticNotation"])
                    PhoneticSpelling = str(getMeaning['results'][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticSpelling"])

                    self.db.insert({ "word" : wordX.lower(), "definition" : definition, "lex_category" : LexCategory , "phonetic_spelling": PhoneticSpelling, "phonetic_definition": PhoneticDefinition})

                    self.resultOut(results, "Definition: "+ query, "{}: {} || {} || PhoneticDefinition: {}".format(DialectType, PhoneticSpelling, LexCategory, PhoneticDefinition))

                else:

                    self.resultOut(results, query + " (word unreachable)", "Please check internet connection")
                    #end of status code
                """
            self.resultOut(results, title= query + " [inside split 0]", subtitle= query)

        self.resultOut(results, title= query + " [last]", subtitle= query)

        results.append({
            "Title": query,
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/app.ico",
            "ContextData": "ctxData"
            # "ContextData": self.dataCTXDict
        })

        return results

    def context_menu(self, data):
        results = []

        # "SubTitle": "{} : {}".format(k, v),

        results.append({
            "Title": "ID",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })

        return results

    def meaning(self, word):
        print("OxfordDictionaryAPI")
        # getMeaning = requests.get(url = self.BASE_URL + self.entries + self.LANGUAGE_CODE + word.lower(), headers = {"app_id": self.APP_ID, "app_key": self.APP_KEY})
        getMeaning = b'{ \n    "id": "confectioner", \n    "metadata": {\n        "operation": "retrieve",\n        "provider": "Oxford University Press",\n        "schema": "RetrieveEntry"\n    },\n    "results": [\n        {\n            "id": "confectioner",\n            "language": "en-us",\n            "lexicalEntries": [\n                {\n                    "entries": [\n                        {\n                            "senses": [\n                                {\n                                    "definitions": [\n                                        "a person whose occupation is making or selling candy and other sweets."\n                                    ],\n                                    "domains": [\n                                        {\n                                            "id": "sweet",\n                                            "text": "Sweet"\n                                        }\n                                    ],\n                                    "id": "m_en_gbus0209730.005",\n                                    "shortDefinitions": [\n                                        "person whose trade is making or selling confectionery"\n                                    ]\n                                }\n                            ]\n                        }\n                    ],\n                    "language": "en-us",\n                    "lexicalCategory": {\n                        "id": "noun",\n                        "text": "Noun"\n                    },\n                    "pronunciations": [\n                        {\n                            "audioFile": "http://audio.oxforddictionaries.com/en/mp3/xconfectioner_us_1.mp3",\n                            "dialects": [\n                                "American English"\n                            ],\n                            "phoneticNotation": "respell",\n                            "phoneticSpelling": "k\xc9\x99n\xcb\x88fekSH(\xc9\x99)n\xc9\x99r"\n                        },\n                        {\n                            "audioFile": "http://audio.oxforddictionaries.com/en/mp3/xconfectioner_us_1.mp3",\n                            "dialects": [\n                                "American English"\n                            ],\n                            "phoneticNotation": "IPA",\n                            "phoneticSpelling": "k\xc9\x99n\xcb\x88f\xc9\x9bk\xca\x83(\xc9\x99)n\xc9\x99r"\n                        }\n                    ],\n                    "text": "confectioner"\n                }\n            ],\n            "type": "headword",\n            "word": "confectioner"\n        }\n    ],\n    "word": "confectioner"\n		}'
        # getMeaning = str(getMeaning, encoding='utf-8')
        getMeaning = json.loads(getMeaning, encoding='utf-8')

        # return getMeaning
        return (getMeaning['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])


if __name__ == "__main__":

    PrateekDictionary()


