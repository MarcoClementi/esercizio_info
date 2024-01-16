book = {
  "title":"Pinocchio",
  "author":"Carlo_Collodi" ,
  "year_published":1883
}

book["type"] = "Romance"

book["year_published"] = "1883"

del book["author"]

for key in book.keys():
    print(key)
    
for value in book.values():
    print(value)
    
for value in book.items():
    print(key, ":" , value)  
  
    