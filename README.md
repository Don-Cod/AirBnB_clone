 Welcome to the AirBnB clone project!
 Python
#DESCRIPTION
# This repository holds a command interpreter and classes (i.e. BaseModel class and several other classes that inherit from it: Amenity, City, State, Place, Review), and a command interpreter. The command interpreter, like a shell, can be activated, take in user input, and perform certain tasks to manipulate the object instances methods and attributes.
# Command Interpreter
-put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
-create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-create the first abstracted storage engine of the project: File storage.
-create all unittests to validate all our classes and storage engine
#Usage
Interactive Mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
 Non-Interactive Mode
 $ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
 #Environment
 Language: Python3
OS: Ubuntu 20.04 LTS
