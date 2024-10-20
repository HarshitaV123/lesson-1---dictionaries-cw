## creating a dictionary 
states= {"chicago":"springfield","florida":"tallahase","indiana":"indianapolis","texas":"austin"}
print(states)
## accesing values from dictionary
my_state=states["indiana"]
print(f"I live in {my_state}")
## creating a list
flowers=["roses","daises","tulips","sunflowers"]
fav_flower=flowers[2]
print(f"My favorite flowers are {fav_flower}")
## getting the list of keys
key_list=list(states.keys())
print(key_list)
## getting the list of values
value_list=list(states.values())
print(value_list)
## looping through the keys
for key in states:
    print(key)
## looping and accessing the values
for key in states:
    print(states[key])
## checking if a key exists in the dictionary 
if "indiana" in states:
    print(f"The capital of Indiana is {states['indiana']}")
else:
    print("This key doesn't exist")
## adding a key value to the dictionary
states["maine"]="augusta"
print(states)
## deleting a key value pair from the dictionary
del(states["florida"])
print(states)
## changing a value in the dictionary
states["texas"]="dallas"
print(states)
## storing a list as a value in the dictionary
states["places"]=["los angeles","new york city","san diego"]
print(states)
## accessing a value from the lists stored in the dictionary
place2=states["places"][1]
print(f"I want to visit {place2}")