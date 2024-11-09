# Write a program that will generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",". 
# These are the 4 objects: 
#   alphabetical strings,
#   real numbers, 
#   integers, 
#   alphanumerics. The alphanumerics should contain a random number of spaces before and after it (not exceeding 10 spaces). 
# The output should be 10MB in size.

import string
import random

def generateAlphabeticalString():
  output = ''
  for i in range(random.randint(1, 10)):            # random length of string
    output += random.choice(string.ascii_letters)   # random alphabet
  return output
  # return ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 10)))  # alternative way


def generateRealNumber():
  return random.uniform(lowerBoundary, upperBoundary)

def generateInteger():
  return random.randint(lowerBoundary, upperBoundary)

def generateAlphanumerics():
  front = " "*(random.randint(0, 10))
  back = " "*(random.randint(0, 10))
  output = ''
  for i in range(random.randint(1, 10)):
    output += random.choice(string.ascii_letters + string.digits)
  return f"{front}{output}{back}"


# Upper and lower boundary for the numeric objects
lowerBoundary = 0
upperBoundary = 100

# Data file configurations
dataFileLimit = 10 * 1024 * 1024 # 10MB
dataFilePath = "Challenge_A.txt"

# Main function
print (f"Writing to {dataFilePath}")

dataFile = open(dataFilePath, "w")

while dataFile.tell() < dataFileLimit: # since we are writing to file, just get the cursor location to know the current file size
  dataFile.write(generateAlphabeticalString() + ",")
  dataFile.write(str(generateRealNumber()) + ",")
  dataFile.write(str(generateInteger()) + ",")
  dataFile.write(generateAlphanumerics() + ",")

dataFile.close()

print (f"Done writing to {dataFilePath}, with size = {dataFile.tell()}")