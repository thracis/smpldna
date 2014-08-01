#class bcolors:
#    A = 'ANSI esc char'
#    T = 'ANSI esc char'
#    C = 'ANSI esc char'
#    G = 'ANSI esc char'
#    do the R/Y/others with same color, different hue

import sys

seq = raw_input("Type your sequence: ")
seq = seq.upper() #capitalizes all letters
seq = seq.replace(" ", "") #gets rid of spaces

#Checks if input contains an invalid character
if not all(x in "AGCT " for x in seq):
    print "Please rerun the program and input a valid DNA sequence"
    sys.exit(1)
if len(seq) <= 1: # check for null or 1bp input
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
    for x in i: #this `for` statement looks at each character in i, calling it x
	if 'A' in x: # that's why you ref x and not i
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
print "GC content is", gc_prcnt, "%. This is FINALLY CORRECT"


# not sure how to include these...
# I think usually the R, Y, N, etc is actually sent out
# so.... R binds with Y, N binds only with ATGC to avoid recuverse and nesting
# What about B, H, D and V? I never see those used, maybe they shouldn't be included
# R can bind H, D can bind W, S, ... 

#R = A or G
#Y = C or T
#N = A or C or G or T
#W = A or T
#S = G or C
#M = A or C
#K = G or T
#B = G or C or T
#H = A or C or T
#D = A or G or T
#V = A or G or C
