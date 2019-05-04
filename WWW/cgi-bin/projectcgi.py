#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable(display = 0, logdir = "/path/to/logdir")

print ("Content-Type: text/html/n")

form = cgi.FieldStorage()

search = form["seqs"].value
searchtype = form.getvalue("searchtype")
name = form["name"].value
mail=  form.getvalue("email")

html = "<html>\n"
html += "<head>\n"
html += "<title> Search Summary </title>\n"
html += "</head>\n\n"
html += "<body>\n"
html += "<h1> This is the summary of your request:</h1>\n"
html += "<p> The submited data <b>" + search + "</b> contains the following details:</p>\n"
html += "<ul>"

for a in searchtype:
   if a == "gene" :
      html += "<li> Gene ID is: </li>\n"
   if a == "product" :
      html += "<li> Protein product name is: </li>\n"
   if a == "source" :
      html += "<li> Chromosomal location is: </li>\n"
   if a == "ACCESSION" :
      html += "<li> Accession code is: </li>\n" 

html += "</ul>\n"
html += "<p> The URL of thsi result page will be in your submitted mail-box within the maximum next hour. </p>\n"
html += "</body>\n"
html += "</html>\n"

print (html)
