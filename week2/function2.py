person1 = {
	"name": "Julia",
	"age": 21,
	"purchases": ["cider", "beer", "wine"],
    "location": ["united states"]
}
person2 = {
	"name": "Jack",
	"age": 18,
	"purchases": ["beer", "beer", "more beer"],
    "location": ["alberta"]
}

legal_drinky = {
	"alberta": 18,
	"ontario": 19,
	"united_states": 21
}

def can_they_buy(person, location):
	name = person["name"]
	age = person["age"]
	items = person["purchases"][0] + ", " + person["purchases"][1] + ", or " + person["purchases"][2]
	if person["age"] < legal_drinky[location]:
		return name + " can't buy " + items
	else:
		return name + " can buy " + items


print(can_they_buy(person1, "united_states"))
# "Julia can buy their cider, beer, and wine."

print(can_they_buy(person2, "alberta"))
# "Jack can buy their beer, beer, and more beer."