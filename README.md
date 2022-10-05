# **Python test task**

This is a Python 3 script,

which performs the following functions:

1. Getting data from a document using the Google API.
2. Data is added to the database.
3. Data for the conversion of $ into rubles are obtained from the Central Bank of the Russian Federation.   
4. The script is constantly running.


Installation
First step clone repositories :
$ gin clone https://github.com/dimasikjitss/Test-task.git

If you have pipenv installed you can just run:

$ pipenv install

Otherwise you can use:

$ pip install -r requirements.txt

Create new table in Postgresql and write data in you meaning:
host = 'your_host'
user = 'your_username'
password = 'your_password'
port = 'your_port'
db_name = "your_DB_name"


You can run server 
