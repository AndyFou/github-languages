from github import Github       #PyGithub: https://github.com/PyGithub/PyGithub
import pdb
import csv
import datetime

csv_file = open("dataset.csv", "w")
me = Github("AndyFou", "********")

user = me.get_user("AndyFou")
#print(user.login, user.public_repos)

languages = {}
for repo in user.get_repos():				# Repos data-type: Repository
	if not repo.fork:
		dict = repo.get_languages()			# Languages data-type: Dictionary
		#print(dict)

		for key in dict.keys():
			if languages.get(key):
				languages[key] += dict[key]
			else:
				languages[key] = dict[key]

#print(languages)


####  INTERESTING

#print(g.get_user("AndyFou").url)
#print(g.get_user("AndyFou").followers_url)
#print(g.get_user("AndyFou").organizations_url)

# print(g.get_user("AndyFou").repos_url) --> https://api.github.com/users/{user}/repos
# Returns JSon Array with Json Object for each repo
# Interesting keys: id, name, languages_url, stargazers_count, {language??}
