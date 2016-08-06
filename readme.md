# Running Python and the webapp2 framework under Apache

## Setup Instructions

### Installation Overview:

Install the following:

* Apache >= 2.4
  * Apache modwsgi
* Python >= 2.7
  * Pip

Follow these steps:

* Create your desired location for the webapp and paste the web folder from this repo there.

* Change into the webapp folder and install python dependencies.

  `pip install -r requirements.txt -t app/lib`

* Copy the [vhost conf]("docs/python-webpp.conf") file from the docs folder to your Apache sites, change the relevant paths (to the web folder you just created) and enable it.

* Restart Apache

The site should now be available at the specified domain from the virtual hosts file.


Full list of install commands I used for setup:

[Installation]("docs/readme.md")
