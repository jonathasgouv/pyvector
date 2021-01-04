# Pyvectorial
The purpose of this module is to create a way of dealing with vectors that is as close to the built-in function as possible, almost as if the vector becomes a new type of variable within Python. I've tried adding all operations with existing vectors, all possible properties. If I have forgotten something please let me know and I will try to implement.

I choose not to implement the plot function since it is possible to easily plot using the matplotlin library, taking the parameters self.x and self.y as input. If you see utility and necessity the function can be implemented in subsequent versions.

Note that all methods work by using vectors represented with coordinates, so if you have a vector
represented as a module and angle, first use the static method Vector.decompose(), and then use the resultant vector with the functions. It is possible to return to the original state using the self.compose method, which will return a list containing the original module and angle.

## Table of Contents
* [Getting Started](#getting-started)
* [Installing](#installing)
* [Built With](#built-with)
* [Documentation](#documentation)
* [Author](#author)
* [License](#license)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installing
You can install it via pip with the command:
```
pip install Vectorial
```
## Built With
* [Python](https://www.python.org/)

## Documentation
### How to call it
For best use the module should be called in the format:
```
from Vectorial import Vector
```
In this way the creation of new vectors is facilitated, as for example:
```
vector1 = Vector(1,3)
vector2 = Vector(2,4)
```

### Print function
The vectors are printed in coordinate format, for example:
```
print (vector1) /// output: (1,3)
```

### Operations
All operations between two vectors work just like any other Python operation, for example:
```
print (vector1 + vector2) /// output: (3,7)
print (vector1 - vector2) /// output: (-1, -1)
print (vector1 * 4) /// output: (4,12)
```
That is, the operation with vectors results in a new vector.
The exception is when we multiply 2 vectors, which returns their internal product:
```
print(vector1 * vector2) /// output: 50.42
```

### Logical operators
#### Greater than (>)
Allows you to use the logical operator "greater than" by comparing the module of the vectors
```
:param other: vector to be compared
:return: True or False
```

#### Less than (<)
It allows the "less than" logical operator to be used by comparing the vector module
```
:param other: vector to be compared
:return: True or False
```

#### Greater or equal (>=)
It allows you to use the logical operator "greater than or equal to" by comparing the vector module
```
:param other: vector to be compared
:return: True or False
```

### Minor or equal (<=)
It allows the logical operator "less than or equal to" to be used by comparing the vector module
```
:param other: vector to be compared
:return: True or False
```

#### Equal (==)
It allows you to use the "equal" logical operator, comparing if two vectors are equal. The vectors will only be considered equal if they have the same module, direction and notion.
```
:param other: vector to be compared
:return: True or False
```

#### Different (!=)
It allows you to use the "different" logical operator, comparing if two vectors are different. The vectors will only be different considering if they have different module, direction or notion.
```
:param other: vector to be compared
:return: True or False
```

### Static functions
Due to the fact that all functions depend on a vector represented in coordinates, it was necessary to create a separate function to deal with vectors represented by magnitude and angle. So if you have a vector that is not represented by coordinates first use the function below. This function will generate the same vector, however represented in coordinates. To return to the original form use the function self.compose() in the new vector.

#### Vecto.decompose(module, angle)
Returns a vector represented with coordinates.
```
print (Vector.decompose(3.16,71.57)) /// output: (1,3)
```

### Functions

To illustrate the use of the functions we will use vector1 (1,3) created at the beginning of this document.

#### self.unit() /// vector1.unit():
Returns the unit vector of this vector, for example:
```
print (vector1.unit()) /// output: (0.3164556962025316,0.9493670886075949)
```

#### self.module() /// vector1.module()
Returns the module of this vector, for example:
```
print (vector1.module()) /// output: 3.16
```

#### self.angle() /// vector1.angle()
Returns the angle formed by the vector and the x-axis, for example:
```
print (vector1.angle()) /// output: 71.57
```

#### self.anglebetween(othervector) /// vector1.anglebetween(vector2)
Returns the angle formed between two vectors, for example:
```
print (vector1.anglebetween(vector2)) /// output: 50.42
```

#### self.compose() /// vector1.compose()
Returns a list containing the module and angle of the vector.
```
print (print (vector1.compose()) /// output: (3.16, 71.57)
```

## Author
* [Jônathas Gouveia](https://github.com/jonathasgouv/)

## License
This project is licensed under the  GPL-3.0 License - see the [LICENSE](https://github.com/jonathasgouv/pyvector/blob/main/LICENSE) file for details
