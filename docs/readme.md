## Installation Commands
###### Install on Debian Jessie

```
apt-get update
apt-get upgrade
apt-get install apache2 libapache2-mod-wsgi

a2enmod wsgi

mkdir -p /var/www/python-webapp/app # Create all required files

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install -r requirements.txt

vim /etc/apache2/sites-available/python-webapp.conf
a2ensite python-webapp.conf
service apache2 restart
```


Example Virtual Hosts file:

```
  <VirtualHost *:80>

    ServerName python-webapp.local.dev
    ServerAdmin email@example.com

    # Replace with path to the web folder containing the app
    DocumentRoot /var/www/python-webapp/

    <Directory /var/www/python-webapp/>
      Require all granted
    </Directory>

    WSGIScriptAlias / /var/www/python-webapp/app/main.wsgi
    Alias /static/ "/var/www/python-webapp/app/static/"

  </VirtualHost>
```
