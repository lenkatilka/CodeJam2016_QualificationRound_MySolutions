
def main():

	import sys
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputJamFile.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + 2*test
		itemsNum = int(content[index])
		index += 1
		items = content[index].split()

		for itemInd in range(2*itemsNum):
			price = int(items[itemInd])
			if price != 0 :
				discount.append(price)
				## find full price
		
		outputStr = "Case #" + str(test+1) + ": "

		pricesStr = " ".join(str(price) for price in discount)
		outputStr += pricesStr
		outputStr += "\n"

		outputFile.write(outputStr)

if __name__ == '__main__':
	main()
