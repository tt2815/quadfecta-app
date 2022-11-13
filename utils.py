import json
import string
import pandas as pd

class Constants:
	configPath = "config.json"

def formatColumnNames(colNameList):
	return {colName: ''.join(colName.translate(str.maketrans('', '', string.punctuation)).split()) for colName in colNameList}

def loadConfig(path):
	return json.loads(open(path).read())

def loadData(path):
	return pd.read_excel(path, engine="openpyxl")