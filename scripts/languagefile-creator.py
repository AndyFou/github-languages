import pdb
import datetime
import csv
import ast
import itertools

# Read data from file and prepare language data for gephi

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

	#NOTE: for the script to work, first row of csv (with labels) should be removed

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
	nodes = {}
	edges = {}

	for user in data:				# Repos data-type: Repository
		top = 3

		# Sort languages and get top
		toplanguages = sorted(user[5],key=user[5].__getitem__,reverse=True)[:top]
		
		for key in toplanguages:			#if not sorted: user[5].keys()
			if nodes.get(key):
				nodes[key] += user[5][key]
			else:
				nodes[key] = user[5][key]

		pairs = itertools.combinations(toplanguages,2)
		for pair in pairs:
			if edges.get(pair):
				edges[pair] += 1
			else:
				edges[pair] = 1

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
	gexf.write('\t\t\t<attribute id="0" title="bytes" type="long"/>\n')
	gexf.write('\t\t</attributes>\n')

	# ADD NODES
	langs = list(nodes.keys())

	gexf.write('\t\t<nodes>\n')
	for key in nodes.keys():
		gexf.write('\t\t\t<node id="' + str(langs.index(key)) + '" label="' + key + '">\n')
		gexf.write('\t\t\t\t<attvalues>\n')
		gexf.write('\t\t\t\t\t<attvalue for="0" value="' + str(nodes[key]) + '"/>\n')
		gexf.write('\t\t\t\t</attvalues>\n')
		gexf.write('\t\t\t</node>\n')
	gexf.write('\t\t</nodes>\n')

	# ADD EDGES
	gexf.write('\t\t<edges>\n')
	i=0
	for (source, target) in edges.keys():
		gexf.write('\t\t\t<edge id="' + str(i) + '" source="' + str(langs.index(source)) + '" target="' + str(langs.index(target)) + '"  weight="' + str(edges[(source,target)]) + '" />\n')	#normalize if weights too big
		i+=1
	gexf.write('\t\t</edges>\n')

	gexf.write('\t</graph>\n')
	gexf.write('</gexf>\n')

	gexf.close()

(nodes,edges) = get_items()
create_gexf(nodes,edges)
