if [ "$(id -u)" != "0" ]; then
	cat<<RARA
This must be run as root

Try using sudo ./uninstall.sh
RARA
else
	rm /usr/bin/webstarter
	rm /usr/bin/websites.txt
fi
