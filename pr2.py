
'''---------------------------------------------------------------------------------------------------

Program file:		pr2.py
Author:				Jorge Martin Joven
Contact:			jmartinjoven@gmail.com
Creation date:		Jul-14th-2019
Description:		This module contains the functions that pr3.py needs to output the files in
					different formats.

Notes: 				Recquires the libraries json, BeautifuSoup, time, and Comment
 
---------------------------------------------------------------------------------------------------'''

import json
import time
from bs4 import BeautifulSoup
from bs4 import Comment


def getTitle(soupObject):

	'''
	Get the title from the soup object. If title is empty 'title = my_page'.
	'''
	
	title = soupObject.title.text  

	if title == '':
		title = 'my_page'

	return title

def getTime():

	'''
	'''

	t = time.strftime('%a, %d %b %Y %H:%M:%S')

	return t


def createHTMLFile( url, soupObject ):

	'''
	Creates a HTML file writing in it the string from the soupObject.
	'''

	my_title = getTitle(soupObject)
	my_time = getTime()

	#Makes BeautifulSoup instances more readable.
	p_soup_html = soupObject.prettify()


	with open('%s.html' %my_title , 'w', encoding= 'utf-8') as file:

		file.writelines('<!--\nWebpage title: ' + my_title + ';\n' + 'Webpage extracted from: ' + url + ';\n' + 'Webpage time extraction: ' + my_time + ';\n' +'-->' + '\n\n')
		file.writelines(p_soup_html)
		file.close()

		

def createTXTFile( url, soupObject ):
	
	'''
	Creates a TEXT file writing in it the string from the soupObject.
	'''

	my_title = getTitle(soupObject)
	my_time = getTime()

	#Makes BeautifulSoup instances more readable.
	p_soup_html = soupObject.prettify()


	with open('%s.txt' %my_title , 'w', encoding= 'utf-8') as file:

		file.writelines('<!--\nWebpage title: ' + my_title + ';\n' + 'Webpage extracted from: ' + url + ';\n' + 'Webpage time extraction: ' + my_time + ';\n' + '-->' + '\n\n')
		file.writelines(p_soup_html)
		file.close()

	

def createXMLFile( url, soupObject ):
	
	'''
	Creates a XML file writing in it the string from the soupObject.
	'''

	my_title = getTitle(soupObject)
	my_time = getTime()

	#Makes BeautifulSoup instances more readable.
	p_soup_html = soupObject.prettify()


	with open('%s.xml' %my_title , 'w', encoding= 'utf-8') as file:

		file.writelines('<!--\nWebpage title: ' + my_title + ';\n' + 'Webpage extracted from: ' + url + ';\n' + 'Webpage time extraction: ' + my_time + ';\n' + '-->' + '\n\n')
		file.writelines(p_soup_html)
		file.close()




def createJSONfile( url, soupObject ):
	
	'''
	Creates a JSON file writing in it the string from the soupObject.
	'''

	my_title = getTitle(soupObject)
	my_time = getTime()

	#Adding comments to the BeautifulSoup object.
	tag = soupObject.html
	new_comment = Comment('\nWebpage title: ' + my_title + ';\n' + 'Webpage extracted from: ' + url + ';\n' + 'Webpage time extraction: ' + my_time + ';\n\n')	
	tag.insert_before(new_comment)

	#Make the soup object readable. 
	p_soup_html = soupObject.prettify()

	#Convert into a JSON.
	y = json.dumps(p_soup_html)

	with open('%s.json' %my_title , 'w', encoding= 'utf-8') as file:

		file.writelines(y)
		file.close()



def createOutputFile(format, url, string ):
	
	'''
	Create a BeautifulSoup object and parses it to html. 
	Converts it into one of the four file formats (html, txt, json, xml)
	given the input format
	'''

	#Creates a BeautifulSoup instance and parses it as html.
	soup_html = BeautifulSoup(string, features="html.parser")
	
	if format == 'html':
		createHTMLFile( url, soup_html )
	elif  format == 'txt':
		createTXTFile( url, soup_html )
	elif format == 'json':
		createJSONfile( url, soup_html )
	elif format == 'xml':
		createXMLFile( url, soup_html )
