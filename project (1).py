import sys
import sympy
from sympy import pretty
def main():
    values =get_values()#gets a dict of values for variables
    units=get_units(values)
    solved, equation =get_result(values)
    if solved:
        print(f"Equation used: {pretty(equation)}")
        for sol in solved:
            print(f"{sol:.2f} {units}")

    else:
        print("No solution found.")

def get_values():
    values = { #create a dict for values
        "vi": None,   # initial velocity
        "vf": None,   # final velocity
        "a": None,    # acceleration
        "d": None,    # displacement
        "t": None,    # time
        "solve": None
    }
    #ask for user input
    values["vi"] = input("What is your initial velocity? enter '?' if unknown ")
    values["vf"] = input("What is your final velocity?, enter '?' if unknown ")
    values["a"] = input("What is your acceleration? enter '?' if unknown ")
    values["t"] = input("What is your total time? enter '?' if unknown ")
    values["d"] = input("What is your displacement? enter '?' if unknown ")
    values["solve"] = input("what are you solving for? ")

    #see if the value for solve key is valid
    valid_inputs = ("vi", "vf", "d", "t", "a")
    if values["solve"] not in valid_inputs:
        sys.exit("Enter a valid variable to solve for (vi, vf, d, t, a)")

    for key, value in values.items():
        if key!="solve" and value != "?":# if value isnt in solve and the value is unknown
            try:
                values[key] = float(value)# convert the values in each key from str->float
            except ValueError:
                sys.exit(f"Invalid number for {key}")
        elif value == "?":
            values[key] = None

 #checks in Solve is already known
    solve_key = values["solve"]
    if values[solve_key] != None:
        sys.exit(f"You cannot provide a value for {solve_key} if you are solving for it")

    return values

def get_result(values):

    vi, vf, a, d = sympy.symbols("vi vf a d")#define symbols
    t = sympy.symbols("t",positive=True)
    variable_symbols = {"vi": vi, "vf": vf, "a": a, "t": t, "d": d}
    #define equationss
    one = sympy.Eq(vf, vi + a*t)
    two=sympy.Eq(d,vi*t+0.5*a*t**2)
    three= sympy.Eq(vf**2,vi**2+2*a*d)
    four=sympy.Eq(d,(vi+vf)/2*t)
    equations=[one,two,three,four]#create a list with equations

    target = variable_symbols[values["solve"]]#convert target into symbol
    for equation in equations: #for each eqauation
        if target in equation.free_symbols: #if target is in the equation
#If all values are present, for each symbol in the equation (except for target)
            if all(values[str(s)] is not None for s in equation.free_symbols if s != target):
                sub={} #substitute values floats into variable_symnols
                for key, value in values.items():
                    if key in variable_symbols and value is not None:
                        sub[variable_symbols[key]] = value #ex: turns "vi" into the actual symbol vi for the equation to use
                solved = sympy.solve(equation.subs(sub), target)
                if target == t:
                    solved = [s for s in solved if s.is_real and s >= 0]
                return solved, equation
            else: continue
    return(None,None)
def get_units(values):
    match values["solve"]:
        case "a":
            return "m/s^2"
        case "vf":
            return "m/s"
        case "vi":
            return "m/s"
        case "d":
            return "m"
        case "t":
            return "s"
        case _:
            return "NONE"

if __name__ == "__main__":
    main()
