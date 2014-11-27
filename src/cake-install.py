#!/usr/bin/python

import argparse
import requests
import zipfile
import sys, os
import shutil
import shlex, subprocess

from requests.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects

def run(args):
	zipurls = {1: 'https://github.com/cakephp/cakephp/archive/1.3.20.zip',
			2: 'https://github.com/cakephp/cakephp/archive/2.5.6.zip',
			3: 'https://github.com/cakephp/app/archive/3.0.0-beta3.zip'}

	sys.stdout.write('Downloading CakePHP...\t\t\t')
	sys.stdout.flush()

	try:	
		results = requests.get(zipurls[args.version])
		if results.status_code == 200:
			output = open('/tmp/file.zip', 'wb')
			output.write(results.content)
			output.close()

			sys.stdout.write('[DONE]\n')

	except IOError as ioe:
		print 'Could not write to the /tmp directory.'
		sys.exit(1)

	except (ConnectionError, HTTPError, Timeout, TooManyRedirects) as re:
		print 'There was a problem downloading CakePHP.'
		sys.exit(1)

	sys.stdout.write('Extracting files...\t\t\t')
	sys.stdout.flush()

	try:
		zippedfile = zipfile.ZipFile('/tmp/file.zip')
		dirname = zippedfile.namelist()[0]
		zippedfile.extractall('/tmp')
		zippedfile.close()
		os.remove('/tmp/file.zip')

	except zipfile.BadZipfile as bzfe:
		print 'Error unzipping CakePHP.'
		sys.exit(1)

	try:
		contentsPath = '/tmp/' + dirname
		names = os.listdir(contentsPath)
		for name in names:
			if os.path.isdir(contentsPath + name):
				shutil.copytree(contentsPath + name, args.dir + '/' + name)
			else:
				shutil.copy2(contentsPath + name, args.dir)
		shutil.rmtree(contentsPath)
		sys.stdout.write('[DONE]\n')

	except shutil.Error as sue:
		print 'Make sure ' + args.dir + ' is writable.'
		sys.exit(1)

	if args.version == 3:
		sys.stdout.write('Running composer...\n\r')
		sys.stdout.flush()

		command = '/usr/local/bin/composer install --prefer-dist -d ' + args.dir + ' --dev'
		commandargs = shlex.split(command)
		proc = subprocess.Popen(commandargs, stderr=subprocess.PIPE)
		if (proc.stderr.read()):
			sys.stdout.write('CakePHP was installed, however composer encountered errors when installing the dependencies. Try running \'composer install\' yourself in the ' + args.dir
				+ ' directory.')
			sys.stdout.flush()
			sys.exit(1)
	
	sys.stdout.write('CakePHP ' + str(args.version) + ' was installed successfully.\n')
	sys.stdout.flush()


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Install a fresh copy of CakePHP.')

	parser.add_argument('--version', default=2, type=int, choices=[1, 2, 3], help='Specify the version of CakePHP you wish to install.')
	parser.add_argument('--dir', default='/vagrant', help='Select the directory where CakePHP will be installed, alter the Apache webroot accordingly.')

	argsObj = parser.parse_args()

	run(argsObj)
