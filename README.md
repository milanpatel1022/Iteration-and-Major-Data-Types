# Iteration-and-Major-Data-Types

This programming assignment is designed to ensure that I know how to use combinations of Python's most important data types to model and compactly write code that solves a wide variety of different programming problems. The kind of abstract thinking that goes into modeling solutions to these programming problems with these data types (and iteration over them) is critical to my development as a computer scientist. I worked on this with a partner for a class assignment.

Reachable File Description:

Prompts the user for the name of a file representing a graph; reads the file (storing the graph in a dictionary); prints the graph/dictionary in a special form; repeatedly prompts the user for a starting node name (rejecting those that are not keys in the graph); computes and prints all the node names that are reachable from it by following zero or more edges in the graph (e.g., a node is reachable from itself).


Finite Automata (FA File) Description:

Prompts the user for the name of a file representing a finite automaton: indicating its states and input->state transitions; reads the information in the file (storing the finite automaton in a dictionary); prints the finite-automaton/dictionary in a special form; prompts the user for the name of a file storing the start-state and inputs to process (each line in the file contains this combination); repeatedly processes these lines, computing the results of the finite automaton on each input, and then prints the results. Note that a finite automaton is really a program; in this problem we are reading a program from a file and then executing it (running the finite automaton) on various inputs. So, we are really writing a compiler/interpreter for a small programming language. A finite automaton (FA) is an machine that is sometimes called a Deterministic Finite Automaton (DFA; see the next problem for an NDFA: a non-deterministic finite automaton). An FA is described by its states and its transitions: each transition for a state specifies an input and what state in the FA that input leads to. We can illustrate an FA as a graph with state labels in circles and edge labels for transitions (see below).


Non-Deterministic Finite Automaton (NDFA File) Description:

Writes the required functions and script that solve, for a Non-Deterministic Finite Automaton, the same problem that was solved for a Deterministic Finite Automaton in Problem #3 (above). Read about the differences between these two automata (below). Adapts code for the FA problem to solve the more general NDFA problem. A non-deterministic finite automaton (NDFA) is machine described by its states and its transitions: each transition for a state specifies an input and a set of states (more than one is allowed) that input can lead to: sets with more than one states is what makes it non-deterministic. We can illustrate a NDFA as a graph with state labels in circles and edge labels for transitions (see below). The critical difference between an FA and an NDFA is that an NDFA can have multiple edges with the same label going to different states (we'll see how to represent and simulate such transitions below).
