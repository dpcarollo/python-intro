def feet_to_inches(feet):
	return feet * 12

table_dimensions_feet = {
	"width": 5,
	"length": 6,
	"height": 3,
}

table_length_inches = feet_to_inches(table_dimensions_feet["length"])
print(table_length_inches)

# Fork is a copy of a repository. 
# A repository is where you keep all components/resources of a project.
# Thus, a Fork is a copy of all the components/resource for a project.
# This is used so you can experiment with changes/fixes, without affecting the project.

# Clone is when a local copy on your computer of a repository.
# Normally, repositories exist remotely (server side).
# With a Clone you can work on a project outside the original location of the repository.
# Any changes made will sync across the original and clones.

price = (20, 6, 9, 14, 5)

hst = 0.13

def get_total(price, tax_percent):
	total = price * (tax_percent + 1)
	total_rounded = round(total, 2)
	return total_rounded

first_total = get_total(price[0], hst)
second_total = get_total(price[1], hst)


print("The first two totals are $" + str(first_total) + " and $" + str(second_total) + " respectively.")

# The first two totals are $22.6 and $6.78 respectively.

