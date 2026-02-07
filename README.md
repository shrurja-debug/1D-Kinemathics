# 1D KINEMATHICS
## Video Demo: https://www.youtube.com/watch?v=ItMETtHHOj8
## Description:
This project is an interactive physics problem solver for 1-dimensional kinematics. It allows the user to input known quantities (initial velocity, final velocity, acceleration, displacement, and time) and specify which variable they would like to solve for.
The program uses **SymPy** to manipulate and solve the standard kinematic equations:
1. (v = v_0 + a t)
2. ( d = v_i t + \tfrac{1}{2} a t^2 )
3. ( v_f^2 = v_i^2 + 2ad )
4. ( d = \tfrac{(v_i + v_f)}{2}t )
## Features
- Interactive input for all 1D kinematics variables (vi, vf, a, d, t)
- Automatically solves for the specified unknown variable
- Handles multiple solution scenarios, including filtering physically valid times
- Provides error handling for invalid inputs or inconsistent values
- Displays results with appropriate SI units
- Includes pytest unit tests for validation

## How it works
1. The program asks the user for each variable (vi, vf, a, d, t).
2. If the variable is unknown, input "?".
3. The user specifies the variable to solve.
4. Validation: The program checks for invalid inputs or contradictions.
5. Equation Selection: The solver automatically picks an equation that includes the target variable and known inputs.
6. Computation: Uses SymPy to substitute known values and solve symbolically.
7. Output: Displays the solution and the equation used, with appropriate units.
## Functions
### <code>get_values()</code> – interacts with the user to collect the values for all kinematic variables (vi, vf, a, d, t).
1. If a value is unknown, the user must input "?", which the function stores as None.
2. It validates that the user inputs either a number or "?" for each variable.
3. It validates that the variable the user wants to solve for is not already given.
4. It validates that the variable to solve for is one of the allowed options (vi, vf, a, d, t).
5. Returns a dictionary containing the user inputs

### <code>get_result(values)</code> –takes the dictionary returned by get_values() and computes the solution for the target variable.
1. It defines symbolic variables for all kinematic quantities using SymPy.
2. It iterates over the four kinematic equations to find one that contains the target variable and has all other required variables known.
2. Substitutes the known numerical values into the selected equation.
3. Uses SymPy to solve the equation for the target variable.
4. If the target variable is time (t), it filters out any negative or complex solutions, ensuring only physically meaningful results.
5. Returns the solution(s) along with the equation used.
6. If an appropriate equation cannot be found and if there isn't sufficient information to do a calculation in one step, the function returns <code>None</code>

### <code>get_units(values)</code> – This function determines the appropriate SI unit for the variable being solved:
- vi or vf → meters per second (m/s)
- a → meters per second squared (m/s²)
- d → meters (m)
- t → seconds (s)
- Returns the corresponding unit as a string, which is used for display in the output.

### <code>main()</code> – main program flow of the solver
1. Calls <code>get_values()</code> to collect and validate user input.
2. Calls <code>get_units()</code> to determine the correct units for the solution.
3. Calls <code>get_result()</code> to compute the solution for the target variable.
4. Prints the equation used and the solution(s) with appropriate units.
5. If <code>get_results</code> returns none, the program prints "No solution Found."

### Files
- project.py – Main solver program.
- test.py – Pytest unit tests for all core functions.
- requirements.txt – Any pip-installable libraries that the project requires (SymPy).
### Requirements
- Python 3.10+
- SymPy 1.14.0
- Pytest (for testing)

