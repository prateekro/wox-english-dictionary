# -*- coding: utf-8 -*-

from wox import Wox
import json
from pprint import pprint
import requests
# from oxford_dictionary_api import OxfordDictionaryAPI
import re
import isafe
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

    def resultOut(self, results, title, subtitle, IcoPath = "Images/app.ico", ContextData = "ctxData"):
        results.append({
            "Title": title,
            "SubTitle": subtitle,
            "IcoPath": IcoPath,
            "ContextData": ContextData
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
            getMeaning = requests.get(url = self.BASE_URL + self.entries + self.LANGUAGE_CODE + query.lower(), headers = {"app_id": self.APP_ID, "app_key": self.APP_KEY})
            # query = self.BASE_URL + self.entries + self.LANGUAGE_CODE + query.lower()
            # getMeaning = b'{ \n    "id": "confectioner", \n    "metadata": {\n        "operation": "retrieve",\n        "provider": "Oxford University Press",\n        "schema": "RetrieveEntry"\n    },\n    "results": [\n        {\n            "id": "confectioner",\n            "language": "en-us",\n            "lexicalEntries": [\n                {\n                    "entries": [\n                        {\n                            "senses": [\n                                {\n                                    "definitions": [\n                                        "a person whose occupation is making or selling candy and other sweets."\n                                    ],\n                                    "domains": [\n                                        {\n                                            "id": "sweet",\n                                            "text": "Sweet"\n                                        }\n                                    ],\n                                    "id": "m_en_gbus0209730.005",\n                                    "shortDefinitions": [\n                                        "person whose trade is making or selling confectionery"\n                                    ]\n                                }\n                            ]\n                        }\n                    ],\n                    "language": "en-us",\n                    "lexicalCategory": {\n                        "id": "noun",\n                        "text": "Noun"\n                    },\n                    "pronunciations": [\n                        {\n                            "audioFile": "http://audio.oxforddictionaries.com/en/mp3/xconfectioner_us_1.mp3",\n                            "dialects": [\n                                "American English"\n                            ],\n                            "phoneticNotation": "respell",\n                            "phoneticSpelling": "k\xc9\x99n\xcb\x88fekSH(\xc9\x99)n\xc9\x99r"\n                        },\n                        {\n                            "audioFile": "http://audio.oxforddictionaries.com/en/mp3/xconfectioner_us_1.mp3",\n                            "dialects": [\n                                "American English"\n                            ],\n                            "phoneticNotation": "IPA",\n                            "phoneticSpelling": "k\xc9\x99n\xcb\x88f\xc9\x9bk\xca\x83(\xc9\x99)n\xc9\x99r"\n                        }\n                    ],\n                    "text": "confectioner"\n                }\n            ],\n            "type": "headword",\n            "word": "confectioner"\n        }\n    ],\n    "word": "confectioner"\n		}'
            if getMeaning.status_code == 200:
                getMeaning = getMeaning.content
                getMeaning = json.loads(getMeaning, encoding='utf-8')
                #Definition
                query = str(getMeaning['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
                ID = str(getMeaning['id'])
                LexCategory = str(getMeaning['results'][0]["lexicalEntries"][0]["lexicalCategory"]["text"])
                DialectType = str(getMeaning['results'][0]["lexicalEntries"][0]["pronunciations"][0]["dialects"][0])
                PhoneticDefinition = str(getMeaning['results'][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticNotation"])
                PhoneticSpelling = str(getMeaning['results'][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticSpelling"])


                self.resultOut(results, "Definition: "+ query, "{}: {} || {} || PhoneticDefinition: {}".format(DialectType, PhoneticSpelling, LexCategory, PhoneticDefinition))

            else:

                self.resultOut(results, query + " (word unreachable)", "Please check internet connection")
                #end of status code

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


