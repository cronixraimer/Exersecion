filename = "dictionaries.py"

with open(filename) as d:
    content = d.readlines()

#print(content)

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)
