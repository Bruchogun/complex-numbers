# Complex Number Calculator

This project implements a complex number calculator in Python, providing various operations and conversions for complex numbers.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

To run this project, you need:

- Python 3.x

### Installing

1. Clone the repository to your local machine.
2. Navigate to the project directory.

No additional installation steps are required as the project uses Python's standard library.

## Features

The complex number calculator supports the following operations:

- Input complex numbers
- Addition
- Subtraction
- Multiplication
- Division
- Calculating the module
- Finding the conjugate
- Converting between Cartesian and polar coordinates
- Calculating the phase

## Running the tests

The project includes a comprehensive test suite. To run the automated tests:

1. Navigate to the project directory.
2. Run the following command:

```
python -m unittest tests.py
```

### Test breakdown

The tests cover all the main functionalities of the complex number calculator:

- Division
- Addition
- Multiplication
- Module calculation
- Conjugate
- Cartesian to polar conversion
- Polar to Cartesian conversion
- Phase calculation
- Subtraction
- Complex number input parsing

Each test checks both the correctness of the result and the expected return type.

## Usage

To use the complex number calculator, import the desired functions from `main.py`. For example:

```python
from main import addition, multiplication, cartesian2polar

# Perform operations
result = addition([3, -6], [5, 7])
print(result)  # Output: [8, 1]

# Convert to polar coordinates
polar = cartesian2polar([3, -6])
print(polar)  # Output: [6.7082, -1.1071]
```

## Built With

* Python 3.x - The programming language used

## Author

* Mauro D'Agostini - [https://github.com/Bruchogun](Bruchogun)

## License

This project is licensed under the MIT - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Inspiration from complex number theory and applications (wink wink).