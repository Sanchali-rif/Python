# Create a Python dictionary of 3 cities and their populations.
# Save it to "cities.json".
# 1. Load the JSON file and print each city and its population.
# 2. Ask the user for a new city and its population, then update the JSON file.

import json
cities={
    "Kolkata":15000000,
    "Mumbai":21000000,
    "Delhi": 33000000
}

with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\cities.json", "w") as f:
    dump=json.dump(cities,f,indent=4)

with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\cities.json", "r") as r:
    load=json.load(r)
    for i in load:
        print(i,":",load[i])

city=input("enter the city name:")
population=int(input("enter the population:"))

load.update({
    city:population
})

with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\cities.json", "w") as newcity:
    addcity=json.dump(load,newcity,indent=4)