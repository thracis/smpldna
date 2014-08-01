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
	    compl.append('\033[1;34mT\033[1;m')
    	if 'T' in x:
	    compl.append('\033[1;31mA\033[1;m')
    	if 'G' in x:
	    compl.append('\033[1;33mC\033[1;m')
    	if 'C' in x:
	    compl.append('\033[1;32mG\033[1;m')

comp(seq)
print "\nThe compliment is", 
print ''.join(compl) 
print "The reverse compliment is",
print ''.join(compl[::-1])

gc_cnt = (g_cnt + c_cnt)
at_cnt = (a_cnt + t_cnt)
print "\n\033[1;32mG\033[1;m\033[1;33mC\033[1;m count is", gc_cnt
print "\033[1;31mA\033[1;m\033[1;34mT\033[1;m count is", at_cnt

total = len(seq)
gc_prcnt = 100 * (float(gc_cnt) / float(total))
print "\n\033[1;32mG\033[1;m\033[1;33mC\033[1;m content is", gc_prcnt, "%."
