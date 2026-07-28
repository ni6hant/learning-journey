from string import ascii_uppercase
#TODO: This long problem! It's still not done
def run(execution_list:list):
    variables_dict = {}
    print_list = []
    i = 0

    for char in ascii_uppercase:
        variables_dict[char] = 0

    if len(execution_list) == 0:
        return print_list

    while True:
        if i == len(execution_list):
            break

        if execution_list[i][:3] == "MOV":
            if execution_list[i][6:] in variables_dict:
                variables_dict[execution_list[i][4:5]] = variables_dict[execution_list[i][6:]]
            else:
                variables_dict[execution_list[i][4:5]] = int(execution_list[i][6:])

        if execution_list[i][:5] == "PRINT":
            if execution_list[i][6:] in variables_dict:
                print_list.append(int(variables_dict[execution_list[i][6:]]))
            else:
                print_list.append(int(execution_list[i][6:]))

        if execution_list[i][:3] == "ADD":
            if execution_list[i][6:] in variables_dict:
                variables_dict[execution_list[i][4:5]] += variables_dict[execution_list[i][6:]]
            else:
                variables_dict[execution_list[i][4:5]] += int(execution_list[i][6:])

        if execution_list[i][:3] == "SUB":
            if execution_list[i][6:] in variables_dict:
                variables_dict[execution_list[i][4:5]] -= variables_dict[execution_list[i][6:]]
            else:
                variables_dict[execution_list[i][4:5]] -= int(execution_list[i][6:])

        if execution_list[i][:3] == "MUL":
            if execution_list[i][6:] in variables_dict:
                variables_dict[execution_list[i][4:5]] *= variables_dict[execution_list[i][6:]]
            else:
                variables_dict[execution_list[i][4:5]] *= int(execution_list[i][6:])

        if execution_list[i][:4] == "JUMP":
            jump_list = execution_list.index(execution_list[i][5:]+":")
            i = jump_list

        if execution_list[i][:2] == "IF":
            special_function = execution_list[i][5:7]
            jump_start_index = execution_list[i].index("JUMP")
            jump_to_value = execution_list[i][jump_start_index + 5:]
            new_jump_index = execution_list.index(jump_to_value+":")
            first_comparator = variables_dict[execution_list[i][3:4]]

            if execution_list[i][7:jump_start_index].strip() in variables_dict:
                second_comparator = variables_dict[execution_list[i][7:jump_start_index].strip()]
            else:
                second_comparator = int(execution_list[i][7:jump_start_index])

            if  special_function == "> ":
                if first_comparator > second_comparator:
                    i = new_jump_index
            if special_function == "< ":
                if first_comparator < second_comparator:
                    i = new_jump_index
            if special_function == "==":
                if first_comparator == second_comparator:
                    i = new_jump_index
            if special_function == "!=":
                if first_comparator != second_comparator:
                    i = new_jump_index
            if special_function == "<=":
                if first_comparator <= second_comparator:
                    i = new_jump_index
            if special_function == ">=":
                if first_comparator >= second_comparator:
                    i = new_jump_index
            pass

        if execution_list[i][:3] == "END":
            break
        i+=1

    return print_list


if __name__ == "__main__":
    program2 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']
    result = run(program2)
    print(result)