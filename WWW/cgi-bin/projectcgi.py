#!/usr/bin/env python3


""" 
This is the CGI script which takes all the entries submited on the HTML to the BL layer to format
and diplay the result in the form of HTML.
--------------------------
Author: FATEMEH KAMALVAND.
--------------------------
"""


import cgi;
import cgitb
cgitb.enable()                               # For troubleshooting
print ("Content-Type: text/html/n")          # Print the HTML MIME-TYPE header




import sys
sys.path.insert(0, "../BL/")
sys.path.insert(0, "../")

import BL_API         # Importing the business logic API
import config         # Importing the config file for DB search (if needed)
form = cgi.FieldStorage()

entries = BL_API.get_all_entries()        # Taking all enteries fron the form
searchtype = form.getvalue("searchtype")  # Defining any entry type
FullName = form.getvalue("FullName")      # Taking the full nime from the HTML from
mail= form.getvalue("email")              # Taking the submitted Email Address from the HTML form


html = "<!DOCTYPE html>"
html += "<html>\n"
html += "<head>\n"
html += "<title> Search Summary </title>\n"
html += "</head>\n\n"
html += "<body>\n"
html += "<h1> This is the list of all entries:</h1>\n"
html += "<p> The submited data <b>" + entry + "</b> contains the following details:</p>\n"
html += "<ul>"

for entry in entries:
   html += "<li>" + entry + "</li>\n"

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
html += "<p> Dear <b>" + name + "</b>, a copy of this result page will be in your submitted mail-box <b>" + mail + " </b> within the maximum next hour. </p>\n"
for name in FullName:        # Process the form
   if "name " not in form:
      name = "none"
   else:
      name = form ["name"].value
   if "mail" not in form:
      mail = "<not given by user>"
   else:
      mail = form ["mail"].value

html += "</body>\n"
html += "</html>\n"

print (html)
