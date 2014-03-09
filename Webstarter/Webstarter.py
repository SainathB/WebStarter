import webbrowser
f=open("websites.txt",'r')
k=f.readline()
while len(k)>0:
	print k
	webbrowser.open(k)
	k=f.readline()
