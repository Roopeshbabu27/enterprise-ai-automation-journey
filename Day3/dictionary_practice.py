thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#print(type(thisdict))

thisdict1 = dict(name = "John", age = 36, country = "Norway")
thisdict1["name"] = 'roopesh'
#thisdict = thisdict1.copy()
print(thisdict)
#print(thisdict["name"])
#print(thisdict.get("name"))
#print(thisdict.keys())

#for x in thisdict.items():
 #   print(x)
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x,y in myfamily.items():
    print(x,y)
print(myfamily["child1"]["name"])

a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers["c2"]["name"])
'''