person = {
   "name": "Duc",
   "age": 21,
   "university": ["FTU"],
   "ex": 3,  
}
# k = list (person.items())
# print(k)
# key: value

#1L read
# print(person)
# print(person["name"])

# loop by key
# for key in person.keys():                 #    .key la chuc nang co san
#     print (key)

# loop by value
# for value in person.values():               #    .values la chuc nang co san
#     print(value)

# loop by items
# for key,value in person.items():
#     print(key,value)

#2 Create or Update
# person["gender"] = "male"
# person["ex"] = 5
# print(person)

#3 Delete
# del person["age"]
# print(person)

# uni = person["university"]
# uni.append("hlu")
# print(person)