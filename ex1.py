print "Enter your unformatted full name"
S = raw_input().split()
x = len(S)
if x == 1 :
	print S[0].title()
elif x == 2 :
	print S[0][0].upper() + "." + " " + S[1].title()
elif x == 3 :
	print S[0][0].upper() + "." + " " + S[1][0].upper() + "." + " " + S[2].title()
