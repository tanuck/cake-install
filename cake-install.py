#!/usr/bin/env python

import argparse
import requests
import zipfile
import sys

def run(args):

	zipurls = {1: 'https://github.com/cakephp/cakephp/archive/1.3.20.zip',
			2: 'https://github.com/cakephp/cakephp/archive/2.5.6.zip',
			3: 'https://github.com/cakephp/app/archive/3.0.0-beta3.zip'}

	sys.stdout.write('Downloading CakePHP...\t\t\t')
	sys.stdout.flush()

	results = requests.get(zipurls[args.version])
	output = open('/home/vagrant/file.zip', 'wb')
	output.write(results.content)
	output.close()
	sys.stdout.write('[DONE]\n')

	sys.stdout.write('Extracting files...\t\t\t')
	sys.stdout.flush()

	zippedfile = zipfile.ZipFile('/home/vagrant/file.zip')
	dirname = zippedfile.namelist()[0]
	zippedfile.extractall('/home/vagrant')
	sys.stdout.write('[DONE]\n')




if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Install a fresh copy of CakePHP.')

	parser.add_argument('--version', default=2, type=int, choices=[1, 2, 3], help='Specify the version of CakePHP you wish to install.')
	parser.add_argument('--dir', default='/vagrant', help='Select the directory where CakePHP will be installed, alter the Apache webroot accordingly.')

	argsObj = parser.parse_args()

	run(argsObj)
