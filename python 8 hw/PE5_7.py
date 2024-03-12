#A
fruits = ["apple", "pear", 'python',]
for item in fruits:
 print(f'{item.title()} is my favorite!')
print(f'I want to have more {item}.\n')
#In this display the words came out as a poem form

#B
numbers = [1,2,3,4,5]
for n in numbers:
 print(n)
print('That’s all the numbers in the list.')
print('numbers = ', numbers)
#In this coding there is numbers list in a line goes straight down along witht he numbers thats being list, in a coloum.

#C
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in n:
 print(i, end = '\t')
count += 1
print(f'\nThere are {count} numbers in the list.')
print('n = ', n)
#The numbers are list in a coloum with space between them.

#D
languages = ["c++", "java", "python"]
for code in languages:
 print(code.upper(), end = " | ")
else:
 print("Enjoy coding!")
#The coding shows Java and Python next to each other with a c++ at the front
 
#E
n = -6, 7, 3, -2, 6, 3, 9
print(len(n), max(n), min(n), sum(n), sep = '\n')
print(n.count(3), n.index(3), n[-6:6], sep = '\n')
print(n, sorted(n), sep = '\n')
#The numbers are listed in rows while some is in rows.

#F
a = 2
b = 3
print(type(a+b))
print(type((a+b,)))
print(type(())) 
#when running it the code shows no number but class equals=int,or tuple