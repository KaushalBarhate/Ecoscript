# EcoScript Programming Language

EcoScript is a simple and environmentally-aware programming language designed to provide insights into the energy consumption and carbon footprint of code execution. It offers basic programming constructs, including variables, arithmetic operations, control flow, and more.

## Features
Arithmetic Operations: Supports basic arithmetic operations like addition, subtraction, multiplication, and division.
Control Flow: Includes conditional statements like if, else, and loops like while.
Energy Consumption: Calculates the energy consumed during code execution.
Carbon Footprint: Estimates the carbon footprint associated with running the code.


### Syntax
Variables
Declare and assign variables using the := operator:

```
x := 10;
y := 20;
```

### Arithmetic
Perform arithmetic operations:

```
z := x + y;

```

### Print Function

Print values to the console:
```
PRINT(z);
```

### Control Flow (work in progress)
Use if, else, and while statements:

```
if (z > 10) {
    PRINT(z);
} else {
    PRINT(x);
}

```


## Local Installation
* Clone the repository.
* Install the required dependencies.
* Run the interpreter with your EcoScript file.
```
python run_ecoscript.py example.ecs
```