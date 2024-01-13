import pandas as pd
import json
import functions
import base

def main(user_input):
    routines = pd.read_csv("routines.csv")
    row = routines.loc[routines["routineName"] == user_input]
    funcs = eval(row["functions"].values[0])
    for func in funcs:
        functionName = functions.functions[func[0]]
        try:
            arg1 = func[1]
        except:
            arg1 = ""
        try:
            arg2 = func[2]
        except:
            arg2 = ""
        try:
            arg3 = func[3]
        except:
            arg3 = ""
        try:
            arg4 = func[4]
        except:
            arg4 = ""
        base.runAppleScript(functionName, arg1=arg1, arg2=arg2, arg3=arg3, arg4=arg4)
    return