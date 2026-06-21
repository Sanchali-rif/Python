import json
data = {
    "name": "Sanchali",
    "age": 20,
    "address": {
        "city": "Kolkata",
        "pincode": 700016
    }
}
with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\data.json", "r") as f:
    py_obj=json.load(f)
    print(py_obj)
with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\data2.json", "w") as p:
    json_obj=json.dump(data , p ,indent=4, sort_keys=True) # will overwrite whatever was written in data.json