# Generating a new, simple website
This repository contains only one file, a python code, which generates a simple website for you, so you don't need to waste time on it when starting a new project.

# How to run it
Running it is very simple.
- First of all, put the file in the folder you would like to have your websites.
- Click on the **website_generator.py** file twice.
- If it is running, a window will pop up.
- Answer the question it is requesting for.
- You are done.

# How it works
If the file is opened in a code editor, one can see the entire algorythm. Every step is commented, thus ordinary people can understand the gist of it.

It has different parts:
  - importing modules
  - starting stopwatch
  - generating a html file
  - generating a javascript file
  - generating a styles directory and a css file
  - returning the running time and a "task completed" message

**The html file:**

It is labeled index.html as default html files usually are.
It contains nothing more than the default <html> tag and its most important elements, such as the head part with the default settings,
and the body part.
The head tag contains the link to the stylesheet, the css file /*style.css*/.
The body tag contains the script, the javascript file /*app.js*/.
 
**The javascript file:**

It has only one line, which is a simple *console.log("success")* command.
  
**The css file:**

It is placed in another folder, the styles directory.
It has three formatting settings:
  - sets all paddings to 0;
  - sets all margins to 0;
  - sets an outline (red, 1px, dashed) to all elements for visible editing purposes

# Personal opinion
This code is very simple and if you are interested, you can use it as you wish. I hope I could help someone!

*Will*
