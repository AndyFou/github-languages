from github import Github       #PyGithub: https://github.com/PyGithub/PyGithub
from github import GithubException
import pdb
import csv
import datetime

def main():
	usernames = open("logins-nolang.txt", "r")
	csv_file = open("dataset.csv", "w")
	
	g = Github("AndyFou", "********")
	
	csv_file.write("id;languages\n")

	for line in usernames:
		user = g.get_user(str(line))
		csv_file.write(str(user.id) + ";" + str(get_user_languages(user)) + "\n")

		if user.id%1000 == 0:
			print("Another 1000! ", datetime.datetime.now().time())

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