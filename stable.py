#Submitter: patelmj1(Patel, Milan)
#Partner: rashidf(Rashid, Faizan)
#We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import prompt
import goody
import copy

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    match_pref = {}
    for line in open_file:
        values = line.rstrip().split(';')
        match_pref[values[0]] = [None, values[1:]]
    return match_pref


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    text = ''
    for man in sorted(d.keys(), key=key, reverse=reverse):
        text += '  %s -> %s\n' %(man, d[man])
    return text


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return p1 if (order.index(p1) < order.index(p2)) else p2


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(male, (men.get(male)[0])) for male in men.keys()}


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    if trace==True: print('\nWomen Preferences (unchanging)\n%s' %womens_text)
    men_copy = copy.deepcopy(men)
    unmatched = {male for male in men.keys()}
    while len(unmatched) != 0:
        if trace==True: print('Men Preferences (current)\n%s\nunmatched men = %s' %(dict_as_str(men_copy), unmatched))
        current_man = unmatched.pop()
        preferred_woman = men_copy[current_man][1][0]

        if women[preferred_woman][0] == None:
            if trace==True: print('\n%s proposes to %s who is not matched, ergo accepts the proposal\n' %(current_man, preferred_woman))
            men_copy[current_man][0] = preferred_woman
            men_copy[current_man][1].remove(preferred_woman)
            women[preferred_woman][0] = current_man
            
        elif women[preferred_woman][0] != None:
            if who_prefer(women[preferred_woman][1], current_man, women[preferred_woman][0]) == current_man:
                if trace==True: print('\n%s proposes to %s who is matched, ergo she accepts the proposal (liking her new match better)\n' %(current_man, preferred_woman))
                unmatched.add(women[preferred_woman][0])
                men_copy[women[preferred_woman][0]][0] = None
                women[preferred_woman][0] = current_man
                men_copy[current_man][0] = preferred_woman
                men_copy[current_man][1].remove(preferred_woman)
            else:
                if trace==True: print('\n%s proposes to %s who is matched, ergo she rejects the proposal (liking her current match better)\n' %(current_man, preferred_woman))
                men_copy[current_man][1].remove(preferred_woman)
                unmatched.add(current_man)
    if trace==True: print('algorithm concluded: the final matches = %s' %(extract_matches(men_copy)))
    if trace==False: print('\nthe final matches = %s' %(extract_matches(men_copy)))
    return(extract_matches(men_copy))
        
        
            
        

  
    
if __name__ == '__main__':
    # Write script here
    mens_file = goody.safe_open('Select the file encoding all mens preferences', 'r', 'File cannot be opened')
    womens_file = goody.safe_open('Select the file encoding all womens preferences', 'r', 'File cannot be opened')
    mens_pref = read_match_preferences(mens_file)
    womens_pref = read_match_preferences(womens_file)     
    mens_text = dict_as_str(mens_pref)
    womens_text = dict_as_str(womens_pref)
    print('\nMen Preferences')
    print(mens_text)
    print('Women Preferences')
    print(womens_text)
    trace = prompt.for_bool('Select whether to trace the algorithm[True]', None, 'Please enter True or False')
    final_matches = make_match(mens_pref, womens_pref, trace)
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
