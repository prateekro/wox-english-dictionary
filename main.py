# -*- coding: utf-8 -*-

from wox import Wox
import json
from oxford_dictionary_api import OxfordDictionaryAPI
import re
# from pprint import pprint
#
# with open('data.json') as f:
#     data = json.load(f)
#
# pprint(data)

class PrateekDictionary(Wox):
    with open('dictionary.json') as f:
        data = json.load(f)

    def query(self, query):
        results = []

        if str(query.lower()) == "<thatword>":
            catchOuput = OxfordDictionaryAPI.meaning(query)

            print("contentID: ", catchOuput['id'])
            print("contentDefinition: ", catchOuput['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
            print("contentShortDefinitions: ", catchOuput['results'][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["shortDefinitions"][0])
            print("contentLexicalCategory(Noun, Verb, ...): ", catchOuput['results'][0]["lexicalEntries"][0]["lexicalCategory"]["text"])
            #
            print("contentDialectType: ", catchOuput['results'][0]["lexicalEntries"][0]["pronunciations"][0]["dialects"][0])
            print("contentPhoneticDefinition: ", catchOuput['results'][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticNotation"])
            print("contentPhoneticSpelling: ", catchOuput['results'][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticSpelling"])
            #
            print("contentDialectType: ", catchOuput['results'][0]["lexicalEntries"][0]["pronunciations"][1]["dialects"][0])
            print("contentPhoneticDefinition: ", catchOuput['results'][0]["lexicalEntries"][0]["pronunciations"][1]["phoneticNotation"])
            print("contentPhoneticSpelling: ", catchOuput['results'][0]["lexicalEntries"][0]["pronunciations"][1]["phoneticSpelling"])

        results.append({
            "Title": " Hello ",
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/app.ico",
            "ContextData": "ctxData"
        })
        # results.append({
        #     "Title": "Hello World",
        #     "SubTitle": "Query: {}".format(query),
        #     "IcoPath":"Images/app.ico",
        #     "ContextData": "ctxData"
        # })
        return results

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results

if __name__ == "__main__":
    PrateekDictionary()
