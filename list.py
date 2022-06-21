friends = ["Anurag", "Tom","Alex"]
print(friends)
print(friends[2])
print(friends[1:])
print(friends[:1])

lucky_numbers=[1,4,5,6,3,7,9,9]
luck2 = lucky_numbers.copy()
print(set(luck2))
friends.extend(lucky_numbers)
print(friends)
friends.insert(3,"Nik")
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
print(luck2)
print(lucky_numbers.count(3))
name="Anurag"
print(list(name))

mylist = list()
print(mylist)
for i in lucky_numbers:
    print(i)
if 8 in lucky_numbers:
    print("yes")
else:
    print("no")
print(len(lucky_numbers))
item = luck2.pop()
print(item)
y = luck2.remove(7)
print(y)
print(luck2)
new_list = [0] * 5
print(new_list)
