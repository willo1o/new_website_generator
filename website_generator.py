#import modules for creating new directory
import os

#import modules for calculating running time 
import time

#ask client for name for new directory and create it
new_directory_path =input("Chosen name for the directory (folder) containing the new website: ").strip().replace(" ","_")  
os.mkdir(new_directory_path)
new_directory_path = "./" + new_directory_path  + "/"

#set the starting point
time_stats = time.time()

#generate index.html file
f_html = open((new_directory_path + "index.html"),"w")
f_html.write('<!DOCTYPE html>\n' + '<html lang="en">\n' + '    <head>\n' + '    <meta charset="UTF-8" />\n' + '    <meta http-equiv="X-UA-Compatible" content="IE=edge" />\n' + '    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n' + '    <title>Document</title>\n' + '    <link rel="stylesheet" href="styles/style.css" />\n' + '  </head>\n' + '  <body>\n' + '    <script src="app.js"></script>\n' + '  </body>\n' + '</html>')
f_html.close()

#generate app.js file
f_script = open((new_directory_path + "app.js"),"w")
f_script.write('console.log("success");')
f_script.close()

#generate styles folder
path = new_directory_path + "styles"
os.mkdir(path)

#generate style.css file
f_style = open((new_directory_path + "styles/style.css"), "w")
f_style.write('/*\n' + 'Reference:\n' + '    - #id\n' + '    - .class\n' + '    - tag\n' + '    - .class tag\n' + '    - .class, .class\n' + '    - more combinations\n' + '*/\n\n\n' + '* {\n' + '  padding: 0px;\n' + '  margin: 0px;\n' + '  outline: 1px red dashed;\n' + '}')
f_style.close()

#output: successful generation and running time
print(f"Task completed, files have been generated in under {time.time()-time_stats} seconds")
time.sleep(10)