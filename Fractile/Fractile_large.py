
def main():

	import sys
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputJamFile.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + test
		itemsNum = int(content[index])
		K, C, S = content[index].split()
		K, C, S = int(K), int(C), int(S)


		outputStr = "Case #" + str(test+1) + ": "
		if (K % C == 0 and S < K/C) or (K%C != 0 and S < K/C + 1):
			outputStr += "IMPOSSIBLE\n" 

		else:
			if(K==S or C==1) : outputStr += " ".join(str(ind) for ind in range(1, K+1))
		
			else:
				howMany = int(K/C)

				for ind in range(howMany):
					for prevC in range(1,C+1):
						

				if howMany*C < K : outputStr += " "+str(   )

		outputFile.write(outputStr)

if __name__ == '__main__':
	main()
