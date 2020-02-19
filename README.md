<p align="center">
  <img src="https://i.ibb.co/cD8rdfQ/ERIKA-3.jpg">
</p>

# AirBnB Clone ver. 1:  Console
#### A command interpreter to manage the AirBnB objects.

This is the first step towards building the first full web application: the  **AirBnB clone**. 

This step is important because it will be used to build with all other of the following projects: HTML/CSS templating, database storage, API, front-end integration…

#### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

## Guide
#### How to start it:
To start the command interpreter, you go to the project's directory and run the command:

    ./console.py

![Startup](https://media.giphy.com/media/LrElgtYRDClP8R4zLr/giphy.gif)

#### How to use it & Examples:
##### Create
Creates a new instance and saves it (to the JSON file) and prints the `id`:
Example: `$ create BaseModel`

![Create](https://media.giphy.com/media/THBlFwC4wP1xqKR6eV/giphy.gif)

##### Show
Prints the string representation of an instance based on the class name and `id`:
Example: `$ show BaseModel 1234-1234-1234`

![Show](https://media.giphy.com/media/kDecIPbRobmkKQHbed/giphy.gif)

##### Destroy
Deletes an instance based on the class name and `id` (save the change into the JSON file):
Example: `$ destroy BaseModel 1234-1234-1234`

![Destroy](https://media.giphy.com/media/lNX5Ifd3dOSaxa6ecQ/giphy.gif)

##### All
Prints all string representation of all instances based or not on the class name:
Example: `$ all BaseModel` or `$ all`

![All](https://media.giphy.com/media/ftZFODLVcGD7R90r01/giphy.gif)

##### Update
Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file):
Example: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`

![Update 1](https://media.giphy.com/media/TiDaXq1xhvozepaXoA/giphy.gif)

After adding or updating attribute it shows:

![Show updated instance](https://media.giphy.com/media/ch89AcTIa3ZinQ5YHM/giphy.gif)

## Requirements

### Python Scripts
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `PEP 8`  style (version 1.7 or more)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

### Python Unit Tests
-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder  `tests`
-   You have to use the  [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g "unittest module")
-   All your test files should be python files (extension:  `.py`)
-   All your test files and folders should start by  `test_`
-   Your file organization in the tests folder should be the same as your project
-   e.g., For  `models/base_model.py`, unit tests must be in:  `tests/test_models/test_base_model.py`
-   e.g., For  `models/user.py`, unit tests must be in:  `tests/test_models/test_user.py`
-   All your tests should be executed by using this command:  `python3 -m unittest discover tests`
-   You can also test file by file by using this command:  `python3 -m unittest tests/test_models/test_base_model.py`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case
## Authors
[Robert Deprizio](https://github.com/BD20171998) - robert.deprizio@gmail.com

[Kevin Paul Apostol](https://github.com/kevapostol) - apostolkevin@gmail.com
