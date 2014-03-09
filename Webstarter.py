import webbrowser
f=open("websites.txt",'r')
while k=f.readline():
	print k
	webbrowser.open(k)
