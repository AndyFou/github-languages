import pdb
import csv
import datetime

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
gexf.write('\t\t<nodes>\n')

gexf.write('\t\t\t<node id="0" label="HTML">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="67924"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="1" label="Shell">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="28247"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="2" label="CSS">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="40689"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="3" label="Groff">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="1013"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="4" label="JavaScript">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="2385192"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="5" label="CoffeeScript">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="2592"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="6" label="Emacs Lisp">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="4389"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="7" label="Erlang">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="964166"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="8" label="Java">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="3585"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="9" label="Makefile">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="19276"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="10" label="Ruby">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="911663"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="11" label="C++">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="3138129"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="12" label="Python">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="62005"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="13" label="Perl">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="1552"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t\t<node id="14" label="C">\n')
gexf.write('\t\t\t\t<attvalues>\n')
gexf.write('\t\t\t\t\t<attvalue for="0" value="119069"/>\n')
gexf.write('\t\t\t\t</attvalues>\n')
gexf.write('\t\t\t</node>\n')

gexf.write('\t\t</nodes>\n')

# ADD EDGES
gexf.write('\t\t<edges>\n')
gexf.write('\t\t\t<edge id="0" source="0" target="1"/>\n')
gexf.write('\t\t\t<edge id="1" source="0" target="7"/>\n')
gexf.write('\t\t\t<edge id="2" source="1" target="2"/>\n')
gexf.write('\t\t\t<edge id="3" source="1" target="3"/>\n')
gexf.write('\t\t\t<edge id="4" source="2" target="4"/>\n')
gexf.write('\t\t\t<edge id="5" source="4" target="5"/>\n')
gexf.write('\t\t\t<edge id="6" source="5" target="8"/>\n')
gexf.write('\t\t\t<edge id="7" source="6" target="0"/>\n')
gexf.write('\t\t\t<edge id="8" source="6" target="14"/>\n')
gexf.write('\t\t\t<edge id="9" source="7" target="9"/>\n')
gexf.write('\t\t\t<edge id="10" source="10" target="9"/>\n')
gexf.write('\t\t\t<edge id="11" source="11" target="7"/>\n')
gexf.write('\t\t\t<edge id="12" source="12" target="3"/>\n')
gexf.write('\t\t\t<edge id="13" source="13" target="14"/>\n')
gexf.write('\t\t</edges>\n')

gexf.write('\t</graph>\n')
gexf.write('</gexf>\n')

gexf.close()
