# Stoa Calculator

> Stoa Calculator is a powerful calculator that have everything you need to do any kind of calculations!

[![Generic badge](https://img.shields.io/badge/Version-0.1.9-<COLOR>.svg)](https://pypi.org/project/StoaCalculator/)
[![Windows](https://img.shields.io/badge/OS-Windows-brightgreen.svg)](https://img.shields.io/badge/OS-Windows-brightgreen.svg)
[![Downloads](https://pepy.tech/badge/stoacalculator)](https://pepy.tech/project/stoacalculator)

This calculator can do from basic aritmethic to advanced calculus, we will be releasing more
updates and adding more features, our goal is to make this calculator the most powerful calculator
ever to exist.

![](https://raw.githubusercontent.com/jorgeeldis/StoaCalculator/main/header.png)

## Installation

<!--
OS X & Linux:

```sh
npm install my-crazy-module --save
```
-->

Windows:

```sh
python3 -m pip install stoacalculator
```

## Usage example

We can use Stoa Calculator in many ways, one of the best ways is to use it for trigonometry, statistics and calculus.

```py
import stoacalculator

# Aritmethic
stoacalculator.add_numbers(1,2)
stoacalculator.substract_numbers(1,2)
stoacalculator.multiply_numbers(1,2)
stoacalculator.divide_numbers(1,2)
stoacalculator.pow_numbers(1,2)
stoacalculator.sqr_root(1,2)

# Trigonometry
stoacalculator.sin(4)
stoacalculator.cos(4)
stoacalculator.tan(4)
stoacalculator.asin(4)
stoacalculator.acos(4)
stoacalculator.atan(4)
stoacalculator.sinh(4)
stoacalculator.cosh(4)
stoacalculator.tanh(4)
stoacalculator.asinh(4)
stoacalculator.acosh(4)
stoacalculator.atanh(4)

# Geometry
stoacalculator.areacircle(25)
stoacalculator.areatriangle(25,10,30)
stoacalculator.areasquare(50,10)
stoacalculator.arearectangle(25,10)

# Statistics
list = [1, 2, 5, 6]
stoacalculator.mean(list)
stoacalculator.mode(list)
stoacalculator.median(list)

# Least common divisor & Greatest common divisor
stoacalculator.LCM(6,12)
stoacalculator.GCM(12,24)

# Decimal to Fraction
stoacalculator.D2F(0.25)

# Return the roots of a polynomial
# Example of polynomial: x^2+2x+2
list = [1, 2, 2]
stoacalculator.roots(list)

# Factorial, Absolute, Euclidean Norm
stoacalculator.factorial(52)
stoacalculator.absolute(-10)
stoaclaculator.euclidean(3, 4)

# Largest Integer not greater than x
stoacalculator.less(-24.58)

# Smallest integer greater than or equal to x.
stoacalculator.more(58.99)

# Plotting
import numpy as np
# We recommend to always use 100 linearly spaced numbers
x = np.linspace(-5, 5, 100)
# For trigonometry we recommend to use this configuration
x = np.linspace(-np.pi,np.pi,100)
# Example of formulas
linearformula = 2*x
quadraticformula = 1*x+x**2
cubicformula = 6*x+x**3
trigonometricformula = np.sin(x)
exponentialformula = np.exp(x)
# Usage of formulas
stoacalculator.linearplot(x, linearformula)
stoacalculator.quadraticplot(x, quadraticformula)
stoacalculator.cubicplot(x, cubicformula)
stoacalculator.trigonometricplot(x, trigonometricformula)
stoacalculator.exponentialplot(x, exponentialformula)
stoacalculator.biplot(x, trigonometricformula, exponentialformula)

# Calculus
from sympy import *
# Partial Fractions
x, y, z = symbols('x y z')
stoacalculator.partfrac(1 / x + (3 * x / 2 - 2)/(x - 4))
# Integrals and Derivatives
# We have to make a constant a symbol
x = Symbol('x')
# Now the usage of this module
stoacalculator.derivatives(sin(x)+exp(x)*log(x))
stoacalculator.integrals(sin(x)+exp(x)*log(x))
```

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

You'll only need to install these packages via pip; matlibplot, numpy, sympy, math and statistic modules from python, this program already import all those modules. So you won't need to import them in your code.

```sh
pip install matplotlib
pip install numpy
pip install sympy
pip install math
pip install statistics
```

## Release History

- 0.1.9 (22/12/21)
  - Nineteenth Release `(Partial Fractions, Largest Integer not greater than x, Smallest integer greater than or equal to x.)`
- 0.1.8 (21/12/21)
  - Eighteenth Release `(More Trigonometric Functions (Hyperbolic & Inverse Hyperbolic), Absolute Value & Factorial of a Number, Euclidean Norm between 2 numbers)`
- 0.1.7 (21/12/21)
  - Seventeeth Release `(Return the roots of a polynomial)`
- 0.1.6 (21/12/21)
  - Sixteenth Release `Performance improvements & bug fixes`
- 0.1.5 (21/12/21)
  - Fifteenth Release `(Decimal to Fraction Conversion)`
- 0.1.4 (21/12/21)
  - Fourteenth Release `(Least common divisor & Greatest common divisor)`
- 0.1.3 (21/12/21)
  - Thirteenth Release `Performance improvements & bug fixes`
- 0.1.2 (13/08/21)
  - Twelfth Release `Performance improvements & bug fixes`
- 0.1.1 (13/08/21)
  - Eleventh Release `Performance improvements & bug fixes`
- 0.1.0 (13/08/21)
  - Tenth Release `(Derivatives & Integrals)`
- 0.0.9 (13/08/21)
  - Ninth Release `(Plotting Calculator from Linear to Exponential Equations)`
- 0.0.8 (13/08/21)
  - Eighth Release `Fixed some typos on the script`
- 0.0.7 (13/08/21)
  - Seventh Release `Performance improvements & bug fixes`
- 0.0.6 (13/08/21)
  - Sixth Release `(Basic Statistics (Mean, Mode, Median))`
- 0.0.5 (13/08/21)
  - Fifth Release `(Basic Geometry (Area of basic shapes))`
- 0.0.4 (13/08/21)
  - Fourth Release `(Trigonometric Functions)`
- 0.0.3 (12/08/21)
  - Third Release `(Square Root)`
- 0.0.2 (27/03/21)
  - Second Release `(Powers/Exponents)`
- 0.0.1 (27/03/21)
  - First Release `(Addition, Substraction, Multiplication, Division)`

## Meta

Jorge Eldis ~ [@jorgeeldis](https://twitter.com/jorgeeldis) ~ jorgeeldisg30@gmail.com

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/jorgeeldis/](https://github.com/jorgeeldis/)

## Contributing

1. Fork it (<https://github.com/jorgeeldis/StoaCalculator/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[wiki]: https://github.com/jorgeeldis/StoaCalculator/wiki
