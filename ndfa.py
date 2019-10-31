#Submitter: patelmj1(Patel, Milan)
#Partner: rashidf(Rashid, Faizan)
#We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict
import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    fa_dict = {}
    for line in file:
        try:
            values = line.rstrip().split(';')
            fa_dict[values[0]] = {}
        except:
            fa_dict[values[0]] = {}
        else:
            combined = zip([value for value in values[1::2]], [value for value in values[2::2]])
            for tup in list(combined):
                if tup[0] not in fa_dict[values[0]].keys():
                    fa_dict[values[0]][tup[0]] = {tup[1]}
                else:
                    fa_dict[values[0]][tup[0]].add(tup[1])            
    return fa_dict


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    text = ''
    for transition in sorted(ndfa):
            states = [(inp, sorted(ndfa[transition][inp])) for inp in sorted(ndfa[transition])]
            text += '  %s transitions: %s\n' %(transition, states)
    return text

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    final_lst = [state]
    lst_states = [state]
    for inp in inputs:
        new_states = []
        for state in lst_states:
            if ndfa[state].get(inp) != None:
                for each_state in ndfa[state][inp]:
                    new_states.append(each_state)
        if len(new_states) == 0:
            final_lst.append((inp, set()))
            break
        else:
            final_lst.append((inp, set(new_states)))
            lst_states = new_states
    return final_lst


def interpret(result : [None]) -> str:
    text = 'Start state = %s\n' %(result[0])
    for tup in result[1:]:
        text += '  Input = %s; new possible states = %s\n' %(tup[0], sorted(tup[1]))
    text += 'Stop state(s) = %s\n' %(sorted(result[-1][1]))
    return text




if __name__ == '__main__':
    # Write script here
    ndfa_file = goody.safe_open('Select the file name encoding the Non-Deterministic Finite Automaton', 'r', 'File cannot be opened')
    ndfa_dict = read_ndfa(ndfa_file)
    contents = ndfa_as_str(ndfa_dict)
    print('\nThe Description of the file selected for the Non-Deterministic Finite Automaton')
    print(contents)
    input_file = goody.safe_open('Choose the file name representing the start-states and their inputs', 'r', 'File cannot be opened')
    for line in input_file:
        values = line.rstrip().split(';')
        ndfa_result = process(ndfa_dict, values[0], values[1:])
        print(interpret(ndfa_result))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
