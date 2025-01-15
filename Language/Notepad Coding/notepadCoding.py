from Coding import *

# Nothing 2 See Here

terminal_input = input("main_program\\terminal\\input>")

if terminal_input[:3] == "run" :
    code = Code(terminal_input[4:])
    code.Run()