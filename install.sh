#!/bin/sh
sudo apt-get update
sudo apt-get -y install apache2
sudo apt-get -y install nginx
sudo apt-get -y install sysstat
sudo apt-get -y install bc
sudo a2enmod cgi
sudo mkdir /var/www/html/sysinfo
sudo cp index.cgi /var/www/html/sysinfo/index.cgi
sudo chmod 755 /var/www/html/sysinfo/index.cgi
sudo cp apache2-sysinfo.conf /etc/apache2/sites-available/apache2-sysinfo.conf
sudo rm /etc/nginx/sites-enabled/default
sudo cp nginx-sysinfo.conf /etc/nginx/sites-enabled/default
sudo rm /etc/apache2/ports.conf
sudo cp ports.conf /etc/apache2/ports.conf 
sudo a2ensite apache2-sysinfo
sudo service apache2 reload
sudo service apache2 restart
sudo touch /var/log/mpstat.log  /var/log/iostat.log  /var/log/tcp.log /var/log/udp.log /var/log/df.log /var/log/network.log
sudo crontab cron.bak
sudo service nginx restart
