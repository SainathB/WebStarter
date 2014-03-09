import webbrowser,os
from sys import argv

def usage():
	print "Webstarter (C) 2014"
	print
	print "Usage:"
	print "\twebstarter help - print this text"
	print "\twebstarter add <url> - add url to list"
	print "\twebstarter list - list all available urls"
	print "\twebstarter open - open all urls in default browser"

argv.pop(0)
argl = len(argv)
if(argl>0):
	if argv[0]=='add':
		if(argl<2):
			print 'Specify a URL to add'
		else:
			os.system("echo "+argv[1]+" >> websites.txt")
	elif argv[0]=='list':
		f=open("./websites.txt",'a+')
		k=f.readline()
		while len(k)>0:
			print k[:-1]
			k=f.readline()
	elif argv[0]=='open':
		f=open("./websites.txt",'a+')
		k=f.readline()
		while len(k)>0:
			print k
			webbrowser.open(k)
			k=f.readline()
	else:
		usage()
else:
	usage()
