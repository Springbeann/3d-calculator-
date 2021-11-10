def askinput(message, length=-1):
    user_input = input(message)
    input_list = user_input.split(",")
    
    if length == -1 or length == len(input_list):
        return input_list
    else:
        return "Input was not the correct length"
