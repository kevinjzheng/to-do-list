# project1-kjz233-ssd410-jpz241-ey667-ehl329
The Project 1 group repo for Kevin J. Zheng, Sm Shihubullah Dipto, Jacob Pace-Zhang, Eugene Yang, and Ethan Haines-LeBlanc.
Project 1 is a to do list

Group Name: A Group  
  
Names and net-ids: ssd410(Sm Shihubullah Dipto) kj3233(Kevin J. Zheng) jpz241(Jacob Pace-Zhang) ey667(Eugene Yang) eh1329(Ethan Haines-LeBlanc)  
  
Public Url: http://ec2-18-216-149-150.us-east-2.compute.amazonaws.com  
  
Brief Description:  
Each item added to the to do webpage should have a unique name so rather than someting like "baseball | baseball" it should be "baseball at 1| baseball at 2" if there will be repeating task names  
The webpage sends and recieves data from the backend through fetch requests which get a JSON object that is onverted into string and then parsed in order to be used by the javascript or just sends a an object as a string to the backend.  
The Flask backend imports Flask in order to have access to various things such as jsonify and render_template.  
The backend imports json as well so as to understand what a json object is.  
The backend also imports pymysql in order to interact with mysql.  
The backend and frontend are run on a AWS where the AWS has set up NGINX and Gunicorn.  
The Flask app has also been set up with NGINX and Gunicorn.  

Project Map:  
projectServer.py - runs the the various routes and allows for data to be sent between the mysql database and the web page that is displayed to the user.  
README.md - is this file and contains all necessary information about the project  
  
templates/ - contains the html file that is displayed by render_template in the flask  
project.html - acts as the frot end for the html web page that is displayed. Directly contains all of its own CSS and  Javascript code.  
  
toDos.sql - the code used to create the mysql database.
