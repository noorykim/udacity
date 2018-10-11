import requests

def read_text(path_to_text_file_in_quotes):
	openfile = open(path_to_text_file_in_quotes) 
	contents = openfile.read()
	# print(contents)

	## check line by line
	# with open(path_to_text_file_in_quotes) as file:
	# 	for line in file:
	# 		check_profanity(line)

	## check the entire file in one shot
	check_profanity(contents)


def check_profanity(text_to_check):
	userdata = {"q": text_to_check}
	resp = requests.get("http://www.wdylike.appspot.com", params=to_query)
	tf = resp.text
	# print(tf)
	if "true" in tf:
		print("alert")
	elif "false" in tf:
		print("no curse words were found")

read_text("C:/.../movie_quotes.txt")
