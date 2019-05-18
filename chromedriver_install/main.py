import os
from chromedriver_install import install
import subprocess


def run():
	path = install(verbose=True, chmod=True)
	if not os.path.exists(path):
		raise FileNotFoundError('The chromedriver executable was not properly downloaded.')
	output = subprocess.check_output([path, '-version']).decode('utf-8')
	print('Version:', output)
	assert 'chromedriver' in output.lower()
	print('Chromedriver is installed at: "%s"' % path)


if __name__ == "__main__":
	run()
