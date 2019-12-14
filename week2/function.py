person1 = {
	"name": "Julia",
	"age": 21,
	"purchases": ["cider", "beer", "wine"]
}
person2 = {
	"name": "Jack",
	"age": 18,
	"purchases": ["beer", "beer", "more beer"]
}

def can_they_buy(person):
	name = person["name"]
	age = person["age"]
	items = person["purchases"][0] + ", " + person["purchases"][1] + ", or " + person["purchases"][2] + " from the store, but they can get it from the hobo down the street for a fiver."
	if age < 19:
		return name + " can't buy " + items
	else:
		return name + " can buy " + items

print(can_they_buy(person1)) 
# "Julia can buy their cider, beer, and wine."

print(can_they_buy(person2)) 
# "Jack cannot buy their beer, beer, and more beer."