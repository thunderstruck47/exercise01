## Ekatte Data

exercise01

### Prerequisites

* [Python](https://www.python.org/downloads/) Runtime for the Python programming language
* [MySQL Sever](https://dev.mysql.com/downloads/mysql/) MySQL Community Server
* [Flask](http://flask.pocoo.org/) A microframework for Python
* [MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html) An interface to MySQL database server for Python

### Installation

Navigate to the "data" folder and run the SQL script.
````
git clone https://github.com/thunderstruck47/exercise01.git
cd exercise01/data/
mysql -u [USER] -p < create_table.sql
````

### Getting Started

Navigate back and start the server

````
cd ../
python server.py
````

###To do:

* Migrate to PostgreSQL and deploy to heroku
* Add interactive map
* Advance searching capability
* Integrate some NSI data
