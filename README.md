# Complex Number Operations

This Python project provides a set of functions to perform various operations on complex numbers. It includes a main script with the implementation of these operations and a test script to verify the correctness of the functions.

## Files

1. `main.py`: Contains the main implementation of complex number operations.
2. `tests.py`: Includes unit tests for the functions defined in `main.py`.

## Features

The project supports the following operations on complex numbers:

- Input of complex numbers
- Addition
- Subtraction
- Multiplication
- Division
- Calculation of modulus
- Conjugate
- Conversion between Cartesian and Polar coordinates
- Phase calculation

## Usage

To use this project, you can import the functions from `main.py` into your own Python script. Here's an example of how to use some of the functions:

```python
from main import inputComplex, addition, multiplication, prettyPrinting

# Input two complex numbers
complex1 = inputComplex()
complex2 = inputComplex()

# Perform operations
sum_result = addition(complex1, complex2)
product_result = multiplication(complex1, complex2)

# Display results
prettyPrinting("Sum:", sum_result)
prettyPrinting("Product:", product_result)
```

## Testing

To run the unit tests, execute the `tests.py` script:

```
python tests.py
```

This will run all the test cases defined in the `TestStringMethods` class.

## Implementation Details

- Complex numbers are represented as lists with two elements: `[real_part, imaginary_part]`.
- Results are rounded to 4 decimal places for precision.
- The project uses the `math` module for trigonometric functions and other mathematical operations.
- Input format for complex numbers: `a+bi` (e.g., `3+4i`)

## Functions

- `inputComplex()`: Prompts user to input a complex number
- `division(complexA, complexB)`: Divides two complex numbers
- `addition(complexA, complexB)`: Adds two complex numbers
- `multiplication(complexA, complexB)`: Multiplies two complex numbers
- `module(complex)`: Calculates the modulus of a complex number
- `conjugate(complex)`: Returns the conjugate of a complex number
- `cartesian2polar(complex)`: Converts from Cartesian to Polar coordinates
- `polar2cartesian(complex)`: Converts from Polar to Cartesian coordinates
- `phase(complex)`: Calculates the phase of a complex number
- `subtraction(complexA, complexB)`: Subtracts two complex numbers
- `prettyPrinting(label, data)`: Prints complex numbers in a readable format

## Contributing

Feel free to fork this project and submit pull requests for any improvements or additional features you'd like to add.

## License

MIT