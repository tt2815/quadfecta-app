import string
def formatColumnNames(colNameList):
	return {colName: ''.join(colName.translate(str.maketrans('', '', string.punctuation)).split()) for colName in colNameList}