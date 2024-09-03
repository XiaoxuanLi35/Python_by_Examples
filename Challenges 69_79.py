# fruit_tuple = ("apple", "banana", "strawberry", "orange")
# print(fruit_tuple.index("strawberry"))
# print(fruit_tuple[2])
#
# names_list = ["John", "Tim", "Sam"]
# del names_list[1]
# names_list.append(input("Add a name: "))
# names_list.sort()
# print(names_list)
#
# colours = {1:"red", 2:"blue", 3:"green"}
# colours [2] = "yellow"
# print(colours)

# x = [154, 634, 892, 345, 341, 43]
# print(len(x))
# print(x[1:4])
# for i in x:
#     print(i)
# num = int(input("Enter number: "))
# if num in x:
#     print(num, "is in the list")
# else:
#     print("Not in the list")
# x.insert(2, 420)
# x.remove(892)
# x.append(993)
# print(x)

# countries_tuple = ("Spain", "Japan", "Portuguese", "Kenya", "Chile")
# print(countries_tuple)
# for i in countries_tuple:
#     print(i)
# chosen_country = input("Choose 1 of these 5 countries: ")
# print(chosen_country)
# print(countries_tuple.index(chosen_country))
# chosen_number = int(input("Choose one num between 0-4: "))
# print(countries_tuple[chosen_number])

sports_lists = ["tennis", "badminton"]
fav_sport = input("What is your favourite sport: ")
sports_lists.append(fav_sport)
sports_lists.sort()
print(sports_lists)
