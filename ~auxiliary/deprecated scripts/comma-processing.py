import csv
import pdb

csvfile = open('data.csv','r')
csvreader = csv.reader(csvfile,delimiter=';')

writefile = open('fixed.csv','w')

for line in csvreader:
	tmp = len(line[2:-2])
	writefile.write(line[0] + "," + line[1] + ",")
	for x in range(tmp):
		if(x!=tmp-1):
			writefile.write(line[x+2] + " -")
		else:
			writefile.write(line[x+2])
	writefile.write("," + line[-2] + "," + line[-1] + "\n")
	
csvfile.close()
writefile.close()