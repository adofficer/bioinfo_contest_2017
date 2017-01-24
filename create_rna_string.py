import random

tetramers = ["AGCU", "AAUU", "AUAU", "ACGU", "UAUA", "UCGA", "UGCA", "UUAA", "CAUG", 
	"CCGG", "CGCG", "CUAG", "GAUC", "GCGC", "GGCC", "GUAC"]
dimers = ["AU", "CG", "GC", "UA"]
monomers = ["A", "U", "G", "C"]

def create_rna_string(k):
	k = int(k) 
	output = ''
	length_output = 0
	while length_output < k:
		if k - length_output > 4:
			output+= random.choice(tetramers)
			length_output += 4
		elif k - length_output >= 2:
			output+= random.choice(dimers)
			length_output +=2
		else:
			output+=random.choice(monomers)
			length_output += 1
			print "rna is almost perfect"
	return output	

print create_rna_string(raw_input(">input desired length of output string:  "))
