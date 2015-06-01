# Requirements
* Tools
    - Vagrant with Virtualbox
    - Python 2.7
    - Postgres 9.1 or higher
    - Virtualenv to manage Python enviernment
    - git
    - The Vagrant box (Contains all of these along with the application)

# How to run the app ?
- Run the Box with Vagrant
- if an error is flashed about folder names. Create python/ and rails/ folders in the
  same directory where the Vagrantfile is located.
- ssh to the box using comman
> $ vagrant ssh
- cd to ~/python/neowave/
- activate the virtualenv using the command
> $ source denv/bin/activate
- the cd into the child directory api/
> $ cd ~/python/neowave/api/
- run the following command
- python manage.py runserver 192.168.100.10:5000
- on your host machine. open the browser and go to 192.168.100.10:5000

