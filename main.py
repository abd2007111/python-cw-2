my_name=input('what is your name')
my_age=input('what is your age')
print(f'my name is{my_name}and I am{my_age} years old')

first_number=int(input("first_number"))
secound_number=int(input ("number two:"))
operation=input("enter an operation:")

if operation=='+':
     print(first_number+secound_number)


elif operation=='-':
    print(first_number-secound_number)

elif operation=='*':
    print(first_number*secound_number)

elif operation=='/':
    print(first_number/secound_number)
else:
    print('the operation is not valid')

bus_capacity=50
people_inbus=int(input'how many people is in the bus')
waiting=int(input'how many people are waiting')
empty_seats=bus_capacity-people_inbus
if empty_seats > waiting:
    print('the empty seats is')
elif empty_seats<= waiting:
    print('there is mno empty seats')