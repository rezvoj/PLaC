# FEI VSB-TUO Programming Languages and Compilers course

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python Version](https://img.shields.io/badge/python-3.10-blue)

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Language Specification](#language-specification)
- [Sample Programs](#sample-programs)
- [Instruction Set](#instruction-set)
- [License](#license)

## Introduction

This project implements a compiler and interpreter for a simple programming language. The compiler is responsible for parsing the input code, performing type checking, and generating stack-based instructions. The interpreter then reads and executes these instructions. The project is written in Python 3.10 and uses the ANTLR4 parser generator.

## Dependencies

Ensure you're using Python version 3.10 or higher.

Install the required dependencies with:
```bash
pip install -r requirements.txt
```

Dependencies used:
- ANTLR4 Python runtime (`antlr4-python3-runtime`)

## Usage

### Compiling a Program

To compile a program, run the `compiler.py` script with the source code file as input:

```bash
python compiler.py <source_file> <compiled_file>
```

- `<source_file>`: The path to the source code file you want to compile.
- `<compiled_file>`: The path where the compiled instructions will be saved.

### Interpreting a Compiled Program

To interpret the compiled program, run the `interpreter.py` script with the compiled file as input:

```bash
python interpreter.py <compiled_file>
```

- `<compiled_file>`: The path to the compiled instructions file.

## Language Specification

### Program Structure

- A program is a sequence of commands.
- Formatting (whitespace, comments, etc.) does not affect the meaning of the program.
- Comments are denoted by `//` and continue to the end of the line.

### Literals

- **int**: A sequence of digits (e.g., `123`).
- **float**: A sequence of digits containing a `.` (e.g., `12.34`).
- **bool**: `true` or `false`.
- **string**: Text enclosed in double quotation marks (e.g., `"hello"`).

### Variables

- Variables must be declared before use.
- Types: `int`, `float`, `bool`, `string`.
- Initial values: `0` for `int`, `0.0` for `float`, `false` for `bool`, and `""` for `string`.

### Statements

- **Declaration**: `type variable1, variable2, ...;`
- **Expression**: Evaluates the expression and discards the result (side effects like variable assignment possible).
- **Input**: `read variable1, variable2, ...;`
- **Output**: `write expression1, expression2, ...;`
- **Block**: `{ statement1 statement2 ... }`
- **Conditional**: `if (condition) statement [else statement]`
- **Loop**: `while (condition) statement`
- **For loop**: `for (expression; condition; expression) statement`

### Expressions

- **Unary Operators**: `-` (negation), `!` (logical NOT)
- **Binary Operators**:
  - Arithmetic: `+`, `-`, `*`, `/`, `%`
  - String concatenation: `.`
  - Relational: `<`, `>`
  - Equality: `==`, `!=`
  - Logical: `&&`, `||`
  - Assignment: `=`

## Sample Programs

The [`samples`](./samples/) directory contains several example programs testing and demonstrating various features of the language:

- `first.lang`: Demonstrates constants, variables, expressions, input/output, and multiple assignments.
- `second.lang`: Demonstrates relational and logical operators.
- `third.lang`: Demonstrates if statements, while loops, and for loops.
- `expressions.lang`: Complex expressions and type conversions.
- `errors.lang`: Examples of syntax and type errors.
- `centroids.lang`: Calculates the centroid of points.
- `primes.lang`: Calculates prime numbers and a "prime string".

## Instruction Set

The compiler generates a stack-based instruction set that the interpreter executes. Below are the instructions:

- **Arithmetic**: `add`, `sub`, `mul`, `div`, `mod`
- **Unary Operations**: `uminus`, `not`, `itof`
- **String Concatenation**: `concat`
- **Logical**: `and`, `or`
- **Relational**: `gt` (greater than), `lt` (less than)
- **Equality**: `eq` (equal)
- **Stack Manipulation**: `push <type> <x>`, `pop`, `load <id>`, `save <id>`
- **Control Flow**: `label <n>`, `jmp <n>`, `fjmp <n>`
- **Input/Output**: `print <n>`, `read <type>`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
