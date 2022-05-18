
#Regular expression
import re

quantity = r"thousand|million|billion"

number = r"\d+(,\d{3})*\.*\d*"
standard = fr"\${number}(-|\sto\s)?({number})?\s({quantity})"

'''
    *  $790 million : word syntax
    *  $12,000      : value syntax
'''

def moneyWord2Value(word):
	quantityValues = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
	return quantityValues.get(word.lower(), 1)

def parseWordSyntax(string):
	replaceString = string.replace(",", "")
	value = float(re.search(number, replaceString).group())
	modifier = moneyWord2Value(re.search(quantity, string, flags=re.I).group())
	return value*modifier

def parseValueSyntax(string):
	replaceString = string.replace(",", "")
	return float(re.search(number, replaceString).group())

def moneyConversion(money):

    # check if type is a list
	if type(money) == list:
		money = money[0]

	word_syntax = re.search(standard, money, flags=re.I)
	value_syntax = re.search(fr"\${number}", money)

	if word_syntax:
		return parseWordSyntax(word_syntax.group())
	elif value_syntax:
		return parseValueSyntax(value_syntax.group())
	else:
		return None

