import re

s = input()

# Split the text using both commas and dots as delimiters
lines = re.split(r'[,.]', s)

# Filter out any empty strings or whitespace
lines = [line.strip() for line in lines if line.strip()]

# Print each line
for line in lines:
    print(line)
