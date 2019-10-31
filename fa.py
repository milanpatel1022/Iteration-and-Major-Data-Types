#Submitter: patelmj1(Patel, Milan)
#Partner: rashidf(Rashid, Faizan)
#We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody


def read_fa(file : open) -> {str:{str:str}}:
    fa_dict = {}
    for line in file:
        values = line.rstrip().split(';')
        combined = zip([inp for inp in values[1::2]], [state for state in values[2::2]])
        fa_dict[values[0]] = dict(combined)
    return fa_dict
        


def fa_as_str(fa : {str:{str:str}}) -> str:
    text = ''
    for state in sorted(fa.keys()):
        text += '  %s transitions: %s\n' %(state, [(inp, fa[state][inp]) for inp in sorted(fa[state].keys())])
    return text
    
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    lst = [state]
    valid_inputs = [valid_inp for valid_inp in fa[state].keys()]
    for inp in inputs:
        if inp not in valid_inputs:
            lst.append((inp, None))
            return lst
        else:
            state = fa[state][inp]
            lst.append((inp, state))
    return lst

def interpret(fa_result : [None]) -> str:
    result = 'Start state = %s\n' %(fa_result[0])
    for i in goody.irange(1, len(fa_result) - 1):
        if fa_result[i][1] == None:
            result += '  Input = %s; illegal input: simulation terminated\n' %(fa_result[i][0])
            result += 'Stop state = %s\n' %(fa_result[i][1])
        else:
            result += '  Input = %s; new state = %s\n' %(fa_result[i][0], fa_result[i][1])
            if i == len(fa_result) - 1:
                result += 'Stop state = %s\n' %(fa_result[i][1])
    return result




if __name__ == '__main__':
    # Write script here
    fa_file = goody.safe_open('Select the file name encoding the Finite Automaton', 'r', 'File cannot be opened')
    fa_dict = read_fa(fa_file)
    fa_str = fa_as_str(fa_dict)
    print('\nThe Description of the file selected for the Finite Automaton')
    print(fa_str)
    start_inp_file = goody.safe_open('Select the file name encoding a sequence of start-states and all their inputs', 'r', 'File cannot be opened')
    print()
    for line in start_inp_file:
        values = line.rstrip().split(';')
        fa_result = process(fa_dict, values[0], values[1:])
        print(interpret(fa_result))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
