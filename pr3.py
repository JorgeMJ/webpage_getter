#!/usr/bin/env python

'''---------------------------------------------------------------------------------------------------

Program file:		pr3.py
Author:				Jorge Martin Joven
Contact:			jmartinjoven@gmail.com
Creation date:		Jul-14th-2019
Description:		This program makes a get request to an url and outputs the webpage into the format
					the user chooses from a given list (html, xml, txt, or json).

Notes: 				Recquires the library requests and the module pr2

					Test webpage http://www.wikipedia.org/wiki/Balanus

---------------------------------------------------------------------------------------------------'''

import requests
import pr2 


## VARIABLE DECLARATION ##

formats_ref = ["html", "txt", "xml", "json", "all"]       #List holding the right formats to the user prompt for formats. 
url=''                                                    #Holds the url the user introduces.


## REQUESTING INFORMATION FROM USER ##

# Prompt the user to introduce a webpage address. 
try:

	url = input('\nEnter the webpage address: ')
	response = requests.get(url)

except requests.exceptions.HTTPError as e:
	
	raise e
		

#Prompt the user to choose the output file/s format/s.
while True:

	input_formats = input('\nEnter the format/s you would like to get your file/s '
	 'from the following list ("html" "txt" "xml" "json" or "all" for all formats): ')

	#Create a list of formats introduced by user in lowecase.
	in_formats = input_formats.lower().split(" ") 

	#Holds the length of 'in_formats' to be compared with 'counter'
	in_formats_len = len(in_formats)
	counter=0

	#Checks if each format introduced by user is valid.
	for f in in_formats:

		if formats_ref.count(f) == 0:

			print('\nPlease, enter valid format/s.\n')

		else:
			counter += 1			

	#If all formats in 'in_formats' are valid, breaks the loop, otherwise keeps re-prompting. 
	if counter == in_formats_len:

		break




## PARSING THE REQUESTED WEBPAGE ##

#Turns the response from the request into a string.
html_doc = response.text



## OBTAING OUTPUT FILES ##

# If the user introduced the keyword 'all', prints every format, else only the selected formats.
if "all" in in_formats:

	for f in ["html", "txt", "xml", "json"]:
		
		pr2.createOutputFile(f, url, html_doc)		
else:

	for f in in_formats:

		pr2.createOutputFile(f, url, html_doc)

		





