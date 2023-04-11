#arthimetric expressions 

# set up three variables with: 2 integers and 1 deimal value
# a,b ,c 

a = 6
b = 2
c = 7.23

# calculate the difference between c and a 
d = c - a 

# format this print statement
# {c} - {a} = answer

print(f"{c} - {a} = {d:.2f}")

print(type(d))

# int, float 

# boolean 
done = False

# string 
msg = "Hi there" 

# side note: type casting 
    # casting a float into an int 
print(int(d))

# Modulus operation 
print(50 % 3)

# loop 
    # initialization 
    # continue condition 
    # update 

# show me a message for each value that is "{value} % 3 = {answer}"
counter = 0
while(counter < 50):
    counter += 1
    print(f"{counter} % 3 = {counter % 3}")

# write a loop that will print starting at 100 
# and decrease by 5 until the value reaches 0 
# once the value reaches zero, print "END" 
number = 100
while(number >= 0): 
    print(number)
    number -= 5 
print("END")

# example of object-oriented 
notDone = True 
while(notDone):
    checkIfDone()