import sys

seq = raw_input("Type your sequence: ")
seq = seq.upper()

if not all(x in "AGCT " for x in seq):
    print "Please rerun the program and input a valid DNA sequence"
    sys.exit(1)
if len(seq) <= 1:
    print "Please rerun the program and input a valid DNA seqence"
    sys.exit(2)

g_cnt = seq.count('G')
c_cnt = seq.count('C')
a_cnt = seq.count('A')
t_cnt = seq.count('T')

print "\nYour sequence is '%s'" % seq
print "It's", len(seq), "base pairs long"

compl = []
def comp(i):
    for x in i:
	if 'A' in x:
	    compl.append('T')
    	if 'T' in x:
	    compl.append('A')
    	if 'G' in x:
	    compl.append('C')
    	if 'C' in x:
	    compl.append('G')

comp(seq)
print "\nThe compliment is", 
print ''.join(compl) 
print "The reverse compliment is",
print ''.join(compl[::-1])

gc_cnt = (g_cnt + c_cnt)
at_cnt = (a_cnt + t_cnt)
print "\nGC count is", gc_cnt
print "AT count is", at_cnt

total = len(seq)
gc_prcnt = 100 * (float(gc_cnt) / float(total))
print "GC content is", gc_prcnt, "%."
