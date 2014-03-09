if [ "$(id -u)" != "0" ]; then
	cat<<RARA
This must be run as root

Try using sudo ./install.sh
RARA
else
	echo Installing..
	cp webstarter/* /usr/bin/
	cat<<RARA
Done!
Now you can use this from anywhere by running the command webstarter
RARA
fi
