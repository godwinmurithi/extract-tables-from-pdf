#Script to scrap tables from a pdf file
#Load the required libraries

import camelot

import os #for ease of manipulating file paths and directories


#Get and set working directory
cd = os.getcwd()
print("current working directory is : {0}" .format(cd))

os.chdir("C:/Users/Godwi/Desktop/Murithi/2023/Geopsy/Projects/Data Scraping")
print("current working directory is : {0}" .format(cd))

#read the pdf file
tables = tabula.read_pdf("2022-KDHS-KIR.pdf", pages = "all")

#Create a new folder named tables where the extracted tables will be exported
foldername = "tables"


#Create a a folder and save the tables
if not os.path.isdir(foldername):
    os.mkdir(foldername)


 # iterate over extracted tables and export as excel individually
for i, table in enumerate(tables, start=1):
    table.to_excel(os.path.join(foldername, f"table_{i}.xlsx"), index=False)
