#Submitter: patelmj1(Patel, Milan)
#Partner: rashidf(Rashid, Faizan)
#We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    x = defaultdict(set)
    for line in file:
        line = line.rstrip().split(';')
        x[line[0]].add(line[1])
    return x
        
        


def graph_as_str(graph : {str:{str}}) -> str:
    text = ''
    for k, v in sorted(graph.items()):
        text += ('  %s -> %s\n' %(k, sorted(v)))
    return text

        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    reached_set = set()
    exploring_list = [start]
    while len(exploring_list) >= 1:
        if trace == True: print('\nreached_set = %s\nexploring_list = %s' %(reached_set, exploring_list))
        any_values = graph.get(exploring_list[0])
        if any_values != None:
            for value in any_values:
                if value not in reached_set:
                    exploring_list.append(value)
        if trace == True: print('removing node from the exploring list/adding it to reached list: node = %s\nafter adding all nodes reachable directly from %s but not already in reached, exploring = %s' %(exploring_list[0], exploring_list[0], exploring_list[1:]))
        reached_set.add(exploring_list.pop(0))
    return reached_set
        


def starting_node(graph : {str:{str}}) -> None:
    while True:
        start_node = str(input('Select the starting node (or select quit): '))
        if start_node.lower() == 'quit':
            break
        else:
            valid_node = graph.get(start_node, "  Entry Error: %s;  Illegal: not a source node\n  Please enter a legal String\n" %start_node)
            if type(valid_node) == set:
                trace = prompt.for_bool('Select whether to trace the algorithm[True]', default=None, error_message='Please enter True or False')
                reached_set = reachable(graph, start_node, trace)
                print('From node %s the reachable nodes = %s\n' %(start_node, reached_set))
            else:
                print(valid_node)
    
    
if __name__ == '__main__':
    file = goody.safe_open('Select the file name encoding the graph', 'r', 'File cannot be opened')
    graph = read_graph(file)
    file.close()
    text = graph_as_str(graph)
    print('\nGraph: node -> [all destination nodes of that node]')
    print(text)
    starting_node(graph)
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
