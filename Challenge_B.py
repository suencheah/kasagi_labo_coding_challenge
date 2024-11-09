# Create a program that will read the generated file above and print to the console the object and its type. Spaces before and after the alphanumeric object must be stripped.

def identifyDataType(obj):
  obj = obj.strip() # strip empty spaces
  if (obj.isdigit()):
    return obj + "- integer\n"
  elif (obj.isalpha()):
    return obj + "- alphabetical string\n"
  elif (obj.isalnum()):
    return obj + "- alphanumeric string\n"
  else:
    return obj + "- real number\n"

# Data file path
inputFilePath = "Challenge_A.txt"
outputFilepath = "/output/Challenge_C.txt"

# Main function
print (f"Reading from {inputFilePath}")

dataFile = open(inputFilePath, "r")
outputFile = open(outputFilepath, "w")

data = dataFile.read().split(',')
for obj in data:
  output= (identifyDataType(obj))
  # print(output)
  outputFile.write(output)

dataFile.close()
outputFile.close()

print("Finished processing data file, output saved to " + outputFilepath)
