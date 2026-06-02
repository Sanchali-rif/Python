info={
    "name":"sanchali",
    "age":19,
    "subject":["Math","data science","oops"],
    3.14:"PI",
    "hobby":"reading"
}
print(info.keys())  #returns all the keys
print(info.values())  #returns all the keys
print(info.items())   #returns all the (key,value) pairs
print(info.get("name"))   #returns value , if value does not exist it returns None
info.update({
    "city":"Kolkata"
})
print(info)