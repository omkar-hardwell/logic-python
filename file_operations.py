# Open a file to read
file = open('demo.txt', 'r')
file1 = open('demo1.txt', 'w')
print("Name of the file:", file.name)

# Read from file
message = file.read()
print(message)

# Write to file
data = input('What is your name: ')
file1.write(data)

# Close file
file.close()
file1.close()
