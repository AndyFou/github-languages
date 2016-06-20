from github import Github       #PyGithub: https://github.com/PyGithub/PyGithub
from github import GithubException
import pdb
import csv
import datetime

def main():
	csv_file = open("dataset.csv", "w")
	g = Github("AndyFou", "********")

	csv_file.write("id,username,location,followers,public_repos\n")

	for user in g.get_users():
		print("\n", user.login, user.public_repos)

		if user.location is not None:
			csv_file.write(str(user.id) + ";" + user.login + ";" + str(user.location.encode('ascii','ignore')) + ";" + str(user.followers) + ";" + str(user.public_repos) + ";" + str(get_user_languages(user)) + "\n")
		if user.id%20 == 0:
			print("Another 20! ", datetime.datetime.now().time())

	csv_file.close()

def get_user_languages(user):
	languages = {}

	for repo in user.get_repos():				# Repos data-type: Repository
		try:
			if not repo.fork:
				dict = repo.get_languages()			# Languages data-type: Dictionary
				#print(dict)

				for key in dict.keys():
					if languages.get(key):
						languages[key] += dict[key]
					else:
						languages[key] = dict[key]
		except GithubException as err:
			print("Unexpected error:", err)

	return languages

main()


#####  IMPORTANT NOTES

# if ("Greece" in user.location) or ("Hellas" in user.location) or ("Athens" in user.location) or ("Athina" in user.location) or ("Thessaloniki" in user.location) or ("Ellada" in user.location) or ("Larisa" in user.location) or ("Giannena" in user.location) or ("Crete" in user.location) or ("Peiraia" in user.location):
#+ str(user.name.encode('ascii','ignore')) + ","

#print(g.get_user("nihilus").id)
#print(g.get_user("nihilus").location)
#print(g.get_user("nihilus").followers)
#print(g.get_user("nihilus").public_repos)
