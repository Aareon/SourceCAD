# SourceCAD
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

SourceCAD is a Python powered CAD/MDT system. Designed with dispatchers and law enforcement in mind, users are able to complete tasks such as call out codes, and other basic law enforcement and dispatcher events.

### Tech
SourceCAD utilizes a number of technologies including, but not limited to:
* [Python 3] - A powerful object oriented programming language, we love it!
* [SQLite] - An ACID-compliant database solution for storing information in a single locally stored file

### Installing from source
SourceCAD requires [Python](https://python.org/) 3.5+ to run.

Clone this repository after installing [Git](https://git-scm.com):
```sh
$ git clone https://github.com/Aareon/SourceCAD
```

### Optional: Create a virtual environment for Python
To maintain a little sanity between dependencies, it's recommended that you use a "virtual environment" for your Python environment.
This can be created and activated like so;
```sh
python3 -m venv [your_virtual_environment_name]
```
Replace the placeholder with whatever name you desire. I'll be using `venv` for the name as that name is pretty standard.

To activate the environment for use in your terminal, simply type the following;
```sh
[your_virtual_environments_path]\\Scripts\\activate
```
Be sure to replace the placeholder with the path to your virtual environments folder. This environment will allow you to use the `python` and `pip` commands for strictly that environment. This environment will remain active so long as that terminal is open, or until you deactivate it.

Install the dependencies after cloning:
#### Unix
```sh
$ cd SourceCAD
$ python3 -m pip install -r requirements.txt
```
#### Windows
```sh
$ cd SourceCAD
$ py -3 -m pip install -r requirements.txt
```

### Development
Want to contribute? We ❤️ pull requests!

### Todos
 - Design login page ✓
 - Account management
 - Design dispatcher resources
 - Design law enforcement resources
 - Discord integration

### Contributors
 - 🐍 Aareon 🐳#0001 - Project lead and Lead of Backend Development
 - harryjoseph#3275 - Lead of Frontend Design and Development, Backend Development Contributor

License
----
GPL
