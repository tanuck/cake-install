cake-install Python Script
==========================

This is a simple Python script to install a fresh copy of CakePHP into a given directory.
It was designed for use with the [tanuck/ubucake](https://vagrantcloud.com/tanuck/boxes/ubucake) vagrant box but could be used on any unix machine
if used correctly.

Installation
------------

_[Git]_

Simply run the command `git clone https://github.com/tanuck/cake-install.git`.

_[Manually]_

1. Download the zip file from: [https://github.com/tanuck/cake-install/zipball/master](https://github.com/tanuck/cake-install/zipball/master)
2. UnZip to a place of your chossing.

Usage
-----

`cake-install [-h] [--version {1,2,3}] [--dir DIR]`

The script is located at `src/cake-install.py`. To run it simply type: `python cake-install.py`
When using the default command arguements, it will try to install CakePHP v2.x into the directory `/vagrant`, as this is the
default setup for the previously mentioned vagrant box. Use the commandline arguments to change this, for example:

- `python cake-install.py --version 3` to install CakePHP 3 (latest dev release) under `/vagrant`.
- `python cake-install.py --version x --dir DIR` to install CakePHP version x under the directory DIR.

Use the `--help` flag for full details.

Global Usage
------------

If you want to be able to use it globally. Move the cake-install.py file to a folder in your $PATH and make sure it is executable. For example:

- `sudo cp src/cake-install.py /usr/local/bin/cake-install && sudo chmod +x /usr/local/bin/cake-install`