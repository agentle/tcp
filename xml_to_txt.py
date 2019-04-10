import time
from subprocess import Popen, PIPE

process = Popen(["./list-eebo-tcp-files", "1483", "1625"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
output = stdout.decode().split("\n")[:-1]

for file in output:
	new_filename = "tcp-alltext/" + file[8:-4] + ".txt"
	print(file)
	print(new_filename)
	args = ["xml/xml-plaintext", "TEI/text", file]
	process = Popen(args, stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
	with open(new_filename, 'a') as f:
		f.write(stdout.decode())
