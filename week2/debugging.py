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