favorite_animals=['dog','cat','monkey','rabbit']
print(favorite_animals)
favorite_animals[1]
favorite_animals.remove('monkey')
favorite_animals.append("sheep")
for animal in favorite_animals:
    print(f"i love {animal}")
numbers=[1,2,3,4,5]
numbers_sum=0
for number in numbers:
    numbers_sum+=number
print(f"the total is {numbers_sum}")