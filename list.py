ratings = [3, 4, 6, 3, 4, 6, 5]

grades = ['A', 'B', 'C', 'D', 'F', 'W', 'P']

list = ["New Your", "Los Angles", "Boston", "Illinois"]

print(list) #prints all elements
print(list[1]) #print second elements

list2 = [1, 3, 4, 6, 4, 7, 8, 2, 0]

print(sum(list2)) #print sum of all elements
print(min(list2)) #print lowest integer in elements
print(max(list2)) #print bigges integer in elements
print(list2[0]) #print first elements
print(list2[-1]) #print last elements

states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','maine','maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ]

print(states) #prints all states in the list

#display all states strating with the letter M

check = 'M'
res = []

for x in states:
     if(x.find(check)==0 or x.find(check.lower())==0): #check if first letter is equal M or lower m
          res.append(x)
#result
print(str(res))
