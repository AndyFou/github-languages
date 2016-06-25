from github import Github       #PyGithub: https://github.com/PyGithub/PyGithub
from github import GithubException
import pdb
import csv
import datetime

# Filter users by location to get only users from a particular country

country = "Greece"

read_file = csv.reader(open("dataset.csv","r"),delimiter=";")			# Read data from
write_file = open(country + ".csv", "w")								# Write data to

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




# LOCATION FILTERS

# GREECE : Greece, Thessaloniki, Athens (but not Georgia or GA or OH), Crete
# ("greece" in line[2].lower()) or ("thessaloniki" in line[2].lower()) or ("crete" in line[2].lower()) or ("athens" in line[2].lower() and not "ga" in line[2].lower() and not "georgia" in line[2].lower() and not "oh" in line[2].lower()):
