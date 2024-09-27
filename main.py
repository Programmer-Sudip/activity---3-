# program to count the number of lines in a text file
# opening a file
file = open("Codingal.txt", "r")
counter = 0

# reading line from the file
Content = file.read()
# splitting the content into lines
CoList = Content.split("\n")

for i in CoList:
    if i:
        counter += 1

print("Number of lines in the file is: ", counter)
print(counter)