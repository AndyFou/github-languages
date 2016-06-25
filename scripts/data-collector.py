from github import Github       #PyGithub: https://github.com/PyGithub/PyGithub
from github import GithubException
import pdb
import csv
import datetime

# Collect data about GitHub users & create file all-data or country-specific-data
# Attributes: id, username, location, followers, public_repos, languages

# FUNCTIONS
#
# collect_data: collects all data and create dataset.csv
# create_country_file: filter data by locations and create data-country.csv
#
# Secondary Functions
# get_user_languages: creates a dictionary of distinct user languages and their bytes (amount of language written per user)
#			returns: languages	type: dictionary (key: language, value: bytes)

def collect_data():
	csv_file = open("dataset.csv", "w")
	g = Github("AndyFou", "********")

	csv_file.write("id;username;location;followers;public_repos;languages\n")

	for user in g.get_users():
		print("\n", user.login, user.public_repos)

		if user.location is not None:
			csv_file.write(str(user.id) + ";" + user.login + ";" + str(user.location.encode('ascii','ignore')) + ";" + str(user.followers) + ";" + str(user.public_repos) + ";" + str(get_user_languages(user)) + "\n")
		if user.id%100 == 0:
			print("Another 100! ", datetime.datetime.now().time())

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

def create_country_file():
	country = "Greece"

	read_file = csv.reader(open("dataset.csv","r"),delimiter=";")			# Read data from
	write_file = open("data-" + country + ".csv", "w")						# Write data to

	write_file.write("id;username;location;followers;public_repos;languages\n")

	for line in list(read_file):
		# filter locations
		if ("greece" in line[2].lower()) or ("thessaloniki" in line[2].lower()) or ("crete" in line[2].lower()) or ("athens" in line[2].lower() and not "ga" in line[2].lower() and not "georgia" in line[2].lower() and not "oh" in line[2].lower()):
			# write filtered users to file
			for x in range(len(line)):
				if x < len(line)-1:
					write_file.write(str(line[x]) + ";")
				else:
					write_file.write(str(line[x]) + "\n")

	write_file.close()

	
# ACTIONS

collect_data()
#create_country_file()



# LOCATION FILTERS

# GREECE : Greece, Thessaloniki, Athens (but not Georgia or GA or OH), Crete
# ("greece" in line[2].lower()) or ("thessaloniki" in line[2].lower()) or ("crete" in line[2].lower()) or ("athens" in line[2].lower() and not "ga" in line[2].lower() and not "georgia" in line[2].lower() and not "oh" in line[2].lower()):
