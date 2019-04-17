import os
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

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


directory = "./tcp-alltext/"
files = []

# get all files
for file in os.listdir(directory):
	if file.endswith(".txt"):
		files.append(file)

# iterate through all files
count = 0

new_file = "sentences_containing_keywords.txt"
with open(new_file, "w") as f_write:
	for file in files:		# REMOVE THIS INDEX FOR FINAL RUN

		keyword_dict = {}
		for word in keywords:
			keyword_dict[word] = []

		count += 1
		if count % 50 == 0:
			print(count)

		path = os.path.join(directory, file)
		with open(path) as f_read:
			data = f_read.read()
			sentences = tokenizer.tokenize(data)	# break up file by sentences
			# for i in range(len(sentences)):
			# 	sentences[i] = ' '.join(c for c in sentences[i] if c not in '\n')
			# print(sentences)
			for sentence in sentences:
				for word in sentence.split(" "):	# split on the spaces
					word = word.rstrip('?:!.,; \n').lower()	# get rid of punctuation
					if word in keywords:
						keyword_dict[word].append(sentence)

		# write read file data to write file
		to_write = ""
		to_write += "File: " + file
		for key, values in sorted(keyword_dict.items()):
			if len(values) > 0:
				to_write += "\n\n--------------------\nKeyword: " + key.title()
				for value in values:
					to_write += "\n----------\n" + value
		to_write += "\n----------------------------------------\n\n"
		f_write.write(to_write)

