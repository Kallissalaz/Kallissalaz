#Five grades can be any numbers (create two grades less than 60). Just make sure to precisely match the output format below.
grade1 = int(input('Enter Grade 1: '))
grade2 = int(input('Enter Grade 2: '))
grade3 = int(input('Enter Grade 3: '))
grade4 = int(input('Enter Grade 4: '))
grade5 = int(input('Enter Grade 5: '))
total =('Grade1' + 'Grade2' + 'Grade3' + 'Grade4' + 'Grade5')
#Calculate average
def calc_average(total):
  return total / 5
