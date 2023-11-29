class TooManyCalculations(ValueError):
    pass

def add_first_op_spaces(value, max_len, position):
    
    spaces = (max_len - len(value)) + 2 # one for space and one for operator
    if position == "T" or position == "E":
        return (" " * 2) + value
    elif position == "B":
        #max - top + white space
        return (" " * spaces) + value #extra space for the space between the operator and the value


def add_seconf_op_spaces(value, operator ,max_len, position):

    spaces = (max_len - len(value)) + 1
    if position == "T":
        return  operator + (" " * spaces) + value
    elif position == "B" or position == "E":
        return operator + " " + value


def add_answer_spaces(spaces, answer):
    answer = str(answer)
    spaces = spaces - len(answer)
    return " " * spaces + str(answer)


def get_max(vals:list):
    """
    position indicates if the position of the max value
    T = top
    B = bottom
    E = equals
    """
    if len(vals[0]) > len(vals[-1]):
        result = len(vals[0])
        position = "T"

    #check bottom is max
    elif len(vals[0]) < len(vals[-1]):
        result = len(vals[-1])
        position = "B"

    #check both the same
    else:
        result = len(vals[0])
        position = "E"

    return result, position


def validations(calculations: list):
    # validations
    """
    assumpsions 
        - there are only 2 operands per value
        - there is a space between the operand and the operator
    """
    # ## VALIDATION
    # max 5 items in the list


    if len(calculations) > 5:
        #raise TooManyCalculations("Error: Too many problems.")
        raise ValueError("Error: Too many problems.")


    # check for only + or - operators
    process_list = list()
    for calc in calculations:
        if "+" in calc:
            process_list.append([calc.split("+"), "+"])
        elif "-" in calc:
            process_list.append([calc.split("-"), "-"])
        else:
            raise ValueError("Error: Operator must be '+' or '-'.")

    # check operands only contain digits  
    for values in process_list:
        lst = [operand for operand in values[0] if not operand.strip().isdigit()]
        if lst:
            raise ValueError("Error: Numbers must only contain digits.")

    # check operators are not longer than 4 digits
    for values in process_list:  
        lst = [operand for operand in values[0] if len(operand.strip()) > 4]
        if lst:
            raise ValueError("Error: Numbers cannot be more than four digits.")


def arithmetic_arranger(calculations: list, show_answer=False):

    try:
        validations(calculations=calculations)

        combined_list = list()

        for calc in calculations:
            temp_list = list()

            string_list = calc.split(" ")

            temp_list.append(string_list[0])
            temp_list.append(string_list[1])
            temp_list.append(string_list[2])
            temp_list.append(eval(calc))

            max_len, position = get_max(string_list)
            temp_list.append(max_len)
            temp_list.append(position)
            combined_list.append(temp_list)

        first_string_list = list()
        second_string_list = list()
        sperator_string_list = list()
        answer_string_list = list()

        for lst in combined_list:

            first_string_list.append(add_first_op_spaces(value=lst[0], max_len=lst[4], position=lst[-1]))
            second_string_list.append(add_seconf_op_spaces(value=lst[2], operator=lst[1], max_len=lst[4], position=lst[-1]))
            sperator_string_list.append("-"* len(add_seconf_op_spaces(value=lst[2], operator=lst[1], max_len=lst[4], position=lst[-1])))
            answer_string_list.append(add_answer_spaces(len(add_seconf_op_spaces(value=lst[2], operator=lst[1], max_len=lst[4], position=lst[-1])),lst[3]))


        # print("    ".join(first_string_list)) 
        # print("    ".join(second_string_list))
        # print("    ".join(sperator_string_list))
        # if show_answer:
        #     print("    ".join(answer_string_list))

        if show_answer:
            result = "    ".join(first_string_list) + "\n" + "    ".join(second_string_list) + "\n" + "    ".join(sperator_string_list) + "\n" + "    ".join(answer_string_list)
        else:
            result = "    ".join(first_string_list) + "\n" + "    ".join(second_string_list) + "\n" + "    ".join(sperator_string_list)

        return result

    except ValueError as e:
        return str(e)