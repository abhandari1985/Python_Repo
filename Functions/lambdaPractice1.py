# we will use lambda function to change one of the element in list to uppercase
# here we take one argument and change it to upper case and return same

countries = ["India", "Japan", "Italy", "France"]
f = lambda x: x.upper()
# f("India")

# Change all the elements in list to upper case
cap_country = []
for country in countries:
    cap_country.append(f(country))
print(cap_country)

# map(function, collection_or_list)
print(list(map(lambda x: x.upper(), countries)))
