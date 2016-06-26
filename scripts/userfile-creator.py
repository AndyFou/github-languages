import pdb
import datetime
import csv
import ast
import itertools

# Read data from file and create user data for gephi

# FUNCTIONS
#
# get_items: read data from file, create nodes (Languages) and edges (pairs of languages)
#			returns: nodes,edges	type: tuple		[nodes/edges type: dictionary (key: language/pair tuple, value: bytes/counter)]
#
# Secondary Functions
# read_datafile: read data from file and create variable Data to keep them
#			returns: data	type: list
# create_gexf: create gexf file with nodes and edges

def read_datafile():
	filename = "dataset"

	csvfile = csv.reader(open(filename + ".csv","r"),delimiter=";")
	data = []

	#NOTES: for the script to work, first row of csv (with labels) should be removed

	for line in list(csvfile):
		user = []
		for x in range(len(line)):
			if x==(len(line)-1):
				user.append(ast.literal_eval(line[x]))	#ast.literal_eval is used to convert string to dictionary
			else:
				user.append(line[x])

			data.append(user)

	return data

def get_items():
	data = read_datafile()

	nodes = {}     #users
	edges = {}     #same language

	# for each user find relations with other users regarding languages
	for source_user in data:
		source_user_langs = sorted(source_user[5],key=source_user[5].__getitem__,reverse=True)[:5]           #sort languages by bytes of code

		# Create Nodes: Users       Key = id, Value = location, followers, repos, languages
		nodes[source_user[0]] = [source_user[1],source_user[2],source_user[3],source_user_langs]
	
		# Create Edges: Languages in common between users      Key = (from_user,to_user), Value = Counter of common languages
		for target_user in data:
			target_user_langs = sorted(target_user[5],key=target_user[5].__getitem__,reverse=True)[:5]       #sort languages by bytes of code
			if source_user[0] is not target_user[0]:

				#compare languages
				for language in target_user_langs:
					if language in source_user_langs:
						if edges.get((source_user[0],target_user[0])):
							edges[(source_user[0],target_user[0])] += 1
						else:
							edges[(source_user[0],target_user[0])] = 1

	return (nodes,edges)

def create_gexf(nodes,edges):
	gexf = open("data.gexf","w")

	# ADD META INFO
	gexf.write('<gexf xmlns="http://www.gexf.net/1.2draft" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd" version="1.2">\n')
	gexf.write('\t<meta lastmodifieddate="' + str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + '">\n')
	gexf.write('\t\t<creator>Antigoni M. Founta</creator>\n')
	gexf.write('\t\t<description>Github Languages Graph</description>\n')
	gexf.write('\t</meta>\n')

	gexf.write('\t<graph defaultedgetype="undirected">\n')

	# ADD ATTRIBUTES
	gexf.write('\t\t<attributes class="node">\n')
	gexf.write('\t\t\t<attribute id="0" title="location" type="string"/>\n')
	gexf.write('\t\t\t<attribute id="1" title="followers" type="int"/>\n')
	gexf.write('\t\t\t<attribute id="2" title="repos" type="int"/>\n')
	gexf.write('\t\t\t<attribute id="3" title="languages" type="string"/>\n')
	gexf.write('\t\t</attributes>\n')

	# ADD NODES
	users = list(nodes.keys())

	gexf.write('\t\t<nodes>\n')
	for key in nodes.keys():
		gexf.write('\t\t\t<node id="' + str(users.index(key)) + '" label="' + key + '">\n')
		gexf.write('\t\t\t\t<attvalues>\n')
		gexf.write('\t\t\t\t\t<attvalue for="0" value="' + str(nodes[key][0]) + '"/>\n')
		gexf.write('\t\t\t\t\t<attvalue for="1" value="' + str(nodes[key][1]) + '"/>\n')
		gexf.write('\t\t\t\t\t<attvalue for="2" value="' + str(nodes[key][2]) + '"/>\n')
		gexf.write('\t\t\t\t\t<attvalue for="3" value="' + str(nodes[key][3]) + '"/>\n')
		gexf.write('\t\t\t\t</attvalues>\n')
		gexf.write('\t\t\t</node>\n')
	gexf.write('\t\t</nodes>\n')

	# ADD EDGES
	gexf.write('\t\t<edges>\n')
	i=0
	for (source, target) in edges.keys():
		gexf.write('\t\t\t<edge id="' + str(i) + '" source="' + str(users.index(source)) + '" target="' + str(users.index(target)) + '"  weight="' + str(edges[(source,target)]) + '" />\n')	#normalize if weights too big
		i+=1
	gexf.write('\t\t</edges>\n')

	gexf.write('\t</graph>\n')
	gexf.write('</gexf>\n')

	gexf.close()


(nodes,edges) = get_items()
create_gexf(nodes,edges)
