# Set (To’plam) mavzusidan masalalar
#1-masala:
fruits = {"apple", "banana"}
result1 = fruits.add("cherry")
print("1-vazifa natijasi:", fruits)
result2 = fruits.remove("banana")
print("2-vazifa natijasi:", fruits)
result3 = fruits.add("kiwi")
print("3-vazifa natijasi:", fruits)
result4 = "apple" in fruits
print("4-vazifa natijasi:","yes" if result4 else "no" )
tropicals = {"pineapple", "banana"}
result5 = fruits.update(tropicals)
print("5-vazifa natijasi:", fruits)
result6 = fruits.discard("banana")
print("6-vazifa natijasi:", fruits)
result7 = fruits.difference(tropicals)
print("7-vazifa natijasi:", result7)
unique_fruits = fruits
result8 = unique_fruits
print("8-vazifa natijasi:", result8)
result9 = sorted(fruits)
print("9-vazifa natijasi:", result9)
print("10-vazifa natijasi:", fruits)


#2-masala:
colors = {"red", "green", "blue"}
result1 = colors.add("yellow")
print("1-vazifa natijasi:", colors)
result2 = colors.discard("green")
print("2-vazifa natijasi:", colors)
result3 = "blue" in colors
print("3-vazifa natijasi:", "Found" if result3 else "Not Found")
extra_colors = {"black", "white", "red"}
print("4-vazifa natijasi:", extra_colors)
result5 = colors.union(extra_colors)
print("5-vazifa natijasi:", result5)
result6 = colors.difference_update(extra_colors)
print("6-vazifa natijasi:", colors)
result7 = colors.intersection(extra_colors)
print("7-vazifa natijasi:", result7)
result8 = len(colors)
print("8-vazifa natijasi:", result8)
new_set = colors.copy()
new_set.clear()
print("9-vazifa natijasi:", new_set)
print("10-vazifa natijasi:", colors)


#3-masala:
students = {'Ali', 'Vali', 'Sami'}
result1 = students.add("Aziz")
print("1-vazifa natijasi:",students)
result2 = students.remove("Sami")
print("2-vazifa natijasi:",students)
result3 = "Jamshid" in students
print("3-vazifa natijasi:","Found" if result3 else "Not Found")
result4 = students.add("Jamshid")
print("4-vazifa natijasi:", students)
new_students = {'Vali', 'Diyor'}
result5 = new_students.update(new_students)
print("5-vazifa natijasi:", fruits)
result6 = students.intersection(new_students)
print("6-vazifa natijasi:",result6)
result7 = students.difference()
print("7-vazifa natijasi:",students)
graduates = {'Ali', 'Jamshid'}
print("8-vazifa natijasi:", graduates)
result9 = students.symmetric_difference(graduates)
print("9-vazifa natijasi:",result9)
print("10-vazifa natijasi:", colors)


#4-masala:
numbers = {1, 2, 3, 4}
result1 = numbers.add(5)
print("1-vazifa natijasi:",numbers)
result2 = numbers.discard(2)
print("2-vazifa natijasi:",numbers)
result3 = 10 in numbers
print("3-vazifa natijasi:","Found" if result3 else "Not Found")
more_nums = {3,6,7}
print("4-vazifa natijasi:",more_nums)
result5 = numbers.update(more_nums)
print("5-vazifa natijasi:",numbers)
result6 = numbers.intersection()
print("6-vazifa natijasi:",numbers)
result7 = numbers.difference(more_nums)
print("7-vazifa natijasi:",result7)
result8 = numbers.union(more_nums)
print("8-vazifa natijasi:",result8)
result9 = max(numbers)
print("9-vazifa natijasi:",result9)
result9 = min(numbers)
print("9-vazifa natijasi:",result9)
print("10-vazifa natijasi:",numbers)


#5-masala:
animals = {'cat', 'dog', 'fish'}
result1 = animals.add("rabbit")
print("1-vazifa natijasi:",animals)
result2 = animals.remove("dog")
print("2-vazifa natijasi:",animals)
result3 = "parrot" in animals
print("3-vazifa natijasi:","Found" if result3 else "Not Found")
result4 = animals.add("parrot")
print("4-vazifa natijasi:",animals)
more_animals = {'lion', 'cat'}
print("5-vazifa natijasi:",more_animals)
result6 = animals.update(more_animals)
print("6-vazifa natijasi:",animals)
result7 = animals.difference()
print("7-vazifa natijasi:",animals)
result8 = sorted(animals)
print("8-vazifa natijasi:",result8)
result9 = len(animals)
print("9-vazifa natijasi:",result9)
print("10-vazifa natijasi:",animals)


















