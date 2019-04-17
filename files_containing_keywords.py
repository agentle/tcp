import os
import unidecode

keywords = [
"Agrippa",
"Allegory",
"Astrology",
"Astronomy",
"Augustine",
"Cicero",
"Divination",
"Drama",
"Epicurean",
"Epicurus",
"Forecast",
"Form",
"Fortune",
"Gods",
"Haruspex",
"Haruspicy",
"Location",
"Magic",
"Manteis",
"Mantis",
"Marvellous",
"Nature",
"Occult",
"Oneiromancy",
"Oracles",
"Paul",
"Petrarch",
"Plutarch",
"Poesy",
"Poetry",
"Predict",
"Prognosticate",
"Prognostication",
"Prophecy",
"Prophesy",
"Prophesying",
"Prophet",
"Providence",
"Providential",
"Revelation",
"Romance",
"Sacred",
"Scripture",
"Sibyl",
"Sibylline",
"Sign",
"Signs",
"Stoic",
"Suetonius",
"Theurgy",
"Tragedy",
"Typology",
"Unseeing",
"Unseen",
"Wonder"]

# convert keywords to lowercase
for i in range(len(keywords)):
	keywords[i] = keywords[i].lower()

keyword_dict = {}
for word in keywords:
	keyword_dict[word] = []

directory = "./tcp-alltext/"
files = []

# get all files
for file in os.listdir(directory):
	if file.endswith(".txt"):
		files.append(file)

# iterate through all files
count = 0
for file in files:		# REMOVE THIS INDEX FOR FINAL RUN

	count += 1
	if count % 50 == 0:
		print(count)

	path = os.path.join(directory, file)
	with open(path) as f:
		for line in f:
			# split by spaces and remove punctuation
			for word in line.split(" "):
				word = word.rstrip('?:!.,;\n').lower()
				# word = unidecode.unidecode(word)	# remove accented characters
				if word in keyword_dict:
					if file not in keyword_dict[word]:
						keyword_dict[word].append(file)

print(keyword_dict)

# write keywords and files to new .txt file
new_file = "files_containing_keywords.txt"
with open(new_file, "w") as f:
	for key, values in sorted(keyword_dict.items()):
		to_write = ""
		to_write += key.title() + ","
		for value in sorted(values):
			to_write += value + ","
		to_write = to_write[:-1] + "\n"
		f.write(to_write)



