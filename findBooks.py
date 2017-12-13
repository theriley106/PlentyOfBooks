import csv
Charles = []
mrKPurchase = []
def csvToList(fileName):
	with open(fileName, 'rb') as f:
	    reader = csv.reader(f)
	    return list(reader)[2:]

primary = csvToList(raw_input("Input primary book list: "))
secondCharles = csvToList(raw_input("Input list after Second and Charles: "))
mrKs = csvToList(raw_input("Input list after Mr. K's: "))


for val in primary:
	if val[0] not in str(secondCharles):
		primary.remove(val)
		Charles.append(val)
	if val[0] in str(secondCharles) and val[0] not in str(mrKs):
		mrKPurchase.append(val)

print("Books Mr. K bought {}".format(len(mrKPurchase)))

raw_input(' ')

print(len(Charles))
