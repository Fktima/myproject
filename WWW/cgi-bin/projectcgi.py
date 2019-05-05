#!/usr/bin/env python3

import cgi
import cgitb; cgitb.enable(display = 0, logdir = "/path/to/logdir")  # for troubleshooting
print ("Content-Type: text/html/n") # Print the HTML MIME-TYPE header


import WWW.cgi-bin.BL-API   #This is importing all the Business Tier API to display the summary list. 

import sys
sys.path.insert(0, "../BL/")
sys.path.insert(0, "../")

import BL-API   # Importing the business logic API
import config   # Importing the config file for DB search
form = cgi.FieldStorage()

search = form["entry"].value
searchtype = form.getvalue("searchtype")
name = form["name"].value
mail=  form.getvalue("email")
enteries = BL-API.getAllEntries()

htnkl += "<!DOCTYPE html>"
html += "<html>\n"
html += "<head>\n"
html += "<title> Search Summary </title>\n"
html += "</head>\n\n"
html += "<body>\n"
html += "<h1> This is the list of all entries:</h1>\n"
html += "<p> The submited data <b>" + search + "</b> contains the following details:</p>\n"
html += "<ul>"

for entry in entries:
   html = "   <li> + entry + </li>\n"

#for a in searchtype:
#   if a == "gene" :
#      html += "<li> Gene ID is: </li>\n"
#   if a == "product" :
#      html += "<li> Protein product name is: </li>\n"
#   if a == "source" :
#      html += "<li> Chromosomal location is: </li>\n"
#   if a == "ACCESSION" :
#      html += "<li> Accession code is: </li>\n" 

html += "</ul>\n"
html += "<p> A copy of thsi result page will be in your submitted mail-box within the maximum next hour. </p>\n"
html += "</body>\n"
html += "</html>\n"

print (html)
