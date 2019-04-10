### Alex Gentle
### April 10, 2019

"""
This simple python script reads in .xml files from EEBO-TCP and converts
them to .txt files using premade conversion methods
"""

from subprocess import Popen, PIPE

# run the list file names command for dates 1483 to 1625
process = Popen(["./list-eebo-tcp-files", "1483", "1625"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()	# store piped output
output = stdout.decode().split("\n")[:-1]

for file in output:
	# build the new filename ([8:-4] cuts off the directory and the .xml extension)
	new_filename = "tcp-alltext/" + file[8:-4] + ".txt"

	# new arguments to be run
	args = ["xml/xml-plaintext", "TEI/text", file]
	process = Popen(args, stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()

	# write plaintext for each .xml file to their corresponding .txt file
	with open(new_filename, 'a') as f:
		f.write(stdout.decode())
