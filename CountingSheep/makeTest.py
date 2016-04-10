

def main():

	outputFile = open("test.txt", "w")
	outputFile.write("1000001\n")

	for i in range(1000001):
		outputFile.write(str(i)+"\n")

	outputFile.close()

if __name__ == "__main__":
	main()
	
