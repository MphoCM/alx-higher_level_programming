0x0C. Python - Almost a circle

This repo contains the implementation of a series of classes in Python that are part of the "Almost a Circle" project. The project focuses on various aspects of Python programming, including object-oriented programming, unit testing, file handling, serialization, and more.

Getting Started
To use these classes, follow the instructions below:


Use the classes in your own Python scripts by importing the necessary modules. For example, to use the Rectangle class, you can import it as follows:
from models.rectangle import Rectangle
Contents
This project consists of the following files and directories:

1. Models: Directory containing the implementation of the classes.

2. Tests: Directory containing unit tests for the classes.
3. README.md: Readme file explaining the project and providing instructions.
4. 1-main.py, 2-main.py, ..., 18-main.py: Example scripts demonstrating the usage of the classes and methods.
5. base.py: Implementation of the Base class.
6. rectangle.py: Implementation of the Rectangle class.
7. square.py: Implementation of the Square class.

Classes
The project includes the following classes:

Base Class
Base: Base class for all other classes in the project. Manages the id attribute and provides methods for JSON serialization and deserialization.
Rectangle Class
Rectangle: Represents a rectangle. Inherits from the Base class. Includes methods for calculating the area, displaying the rectangle, updating attributes, and more.
Square Class
Square: Represents a square. Inherits from the Rectangle class. Includes methods for updating attributes specific to squares.
Testing
The project includes unit tests for each class. To run the tests, use the following command:

python3 -m unittest discover tests
