import sys
import input_parser
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit

'''
Name:   Ruby Liang
SID:    540180464
Unikey: blia0673

run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Returns whether or not '-RUN-MY-CIRCUIT' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i = 0
    while i < len(args):
        if args[i] == "-RUN-MY-CIRCUIT":
            return True
        i += 1
    return False


def is_add_my_mirrors_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Returns whether or not '-ADD-MY-MIRRORS' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i = 0
    while i < len(args):
        if args[i] == "-ADD-MY-MIRRORS":
            return True
        i += 1
    return False


def initialise_circuit() -> LaserCircuit:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Gets the inputs for the board size, emitters and receivers and processes
    it to create a LaserCircuit instance and return it. You should be using
    the functions you have implemented in the input_parser module to handle
    validating each input.

    Returns
    -------
    A LaserCircuit instance with a width and height specified by the user's
    inputted size. The circuit should also include each emitter and receiver
    the user has inputted.
    '''
    #for parsing size of the board 

    print("Creating circuit board...")
    while True:
        try:
            tup = input_parser.parse_size(input("> "))
            # print(f"{tup} type is {type(tup)}")
            width_i, height_i = tup
            # print(width_i)
            # print(height_i)
            building_Circuit = LaserCircuit(width_i, height_i)
            break
        except (TypeError, ValueError) as e:
            print(e)
    print(f"{width_i}x{height_i} board created.\n")
    building_Circuit.print_board()
    #for parsing emitters
    print("Adding emitter(s)...")
    i = 0
    max_emitters = 10
    while i < max_emitters:
        curr_input = input("> ")
        if curr_input == "END EMITTERS":
            break
        try:
            # curr_emitter =  Emitter_list.append(parse_emitter(curr_input))
            curr_emitter =  input_parser.parse_emitter(curr_input)
            # print(curr_emitter)
            building_Circuit.add_emitter(curr_emitter)
            i += 1
        except (TypeError, ValueError) as e:
            print(e)
    print(f"{i} emitter(s) added.\n")

    #for parsing receivers
    print("Adding receiver(s)...")
    j = 0
    max_receivers = 10
    while j < max_receivers:
        curr_input = input("> ")
        if curr_input == "END RECEIVERS":
            break
        try:
            curr_receiver =  input_parser.parse_receiver(curr_input)
            building_Circuit.add_receiver(curr_receiver)
            j += 1
        except (TypeError, ValueError) as e2:
            print(e2)
    print(f"{j} receiver(s) added.\n")
    
    return building_Circuit


def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Handles setting the pulse sequence of the circuit. 
    The lines for the pulse sequence will come from the a file named
    /home/input/<file_name>.in. 
    You should be using the functions you have implemented in the input_parser module 
    to handle validating lines from the file.

    Parameter
    ---------
    circuit - The circuit to set the pulse sequence for.
    file_obj - A file like object returned by the open()
    '''
    f = open(file_obj, "r")
    print("Setting pulse sequence...")
    
    while True:
        line = f.readline().strip()
        if line == "":
            break
        not_set_emm = []
        all_emm = []
        i = 0
        while i < len(circuit.get_emitters()):
            all_emm.append(circuit.get_emitters()[i].get_symbol())
            if not circuit.get_emitters()[i].is_pulse_sequence_set():
                not_set_emm.append(circuit.get_emitters()[i].get_symbol())
            i += 1
        #  Once all emitters have been set, it ends with a concluding message that the pulse sequence has been set
        if not_set_emm == []:
            print("Pulse sequence set.\n")
            break
        else:
            print(f"-- ({', '.join(not_set_emm)})")
        print(line)
        try:
            symbol, frequency, direction = input_parser.parse_pulse_sequence(line)
        except (TypeError, ValueError) as e3:
            print(e3)
            continue

        #check line
        try:
            index2 = all_emm.index(symbol)
        except ValueError:
            print(f"Error: emitter '{symbol}' does not exist")
            continue
        try:
            index1 = not_set_emm.index(symbol)
        except ValueError:
            print(f"Error: emitter '{symbol}' already has its pulse sequence set")
            continue


        #set_pulse_sequence for exist 
        j = 0
        while j < len(circuit.get_emitters()):

            if symbol == circuit.get_emitters()[j].get_symbol():
                circuit.get_emitters()[j].set_pulse_sequence(frequency, direction)
                print(f"{symbol} set!! ")
                break
            j += 1


def add_mirrors(circuit: LaserCircuit) -> None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Handles adding the mirrors into the circuit. You should be using the
    functions you have implemented in the input_parser module to handle
    validating each input. 
    
    Parameters
    ----------
    circuit - the laser circuit to add the mirrors into
    '''
    #for parsing emitters
    print("Adding mirror(s)...")
    i = 0
    # max_emitters = 10
    while True:
        curr_input = input("> ")
        if curr_input == "END MIRRORS":
            break
        try:
            # curr_emitter =  Emitter_list.append(parse_emitter(curr_input))
            curr_mirror =  input_parser.parse_mirror(curr_input)
            print(curr_mirror)
            circuit.add_mirror(curr_mirror)
            i += 1
        except (TypeError, ValueError) as e:
            print(e)
    print(f"{i} mirror(s) added.\n")


def main(args: list[str]) -> None:
    # only requires implementation once you reach GET-MY-INPUTS
    # will require extensions in RUN-MY-CIRCUIT and ADD-MY-MIRRORS
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''

    #remove the line below once you start implementing this function
    LaserCircuit1 = initialise_circuit()
    if is_add_my_mirrors_enabled(sys.argv):
        print("<ADD-MY-MIRRORS FLAG DETECTED!>\n")
        add_mirrors(LaserCircuit1)
    LaserCircuit1.print_board()

    if is_run_my_circuit_enabled(sys.argv):
        print("<RUN-MY-CIRCUIT FLAG DETECTED!>")
    # set_pulse_sequence(LaserCircuit1, "/home/input/pulse_sequence.in")
        try:
            with open('./pulse_sequence', 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print("Error: -RUN-MY-CIRCUIT flag detected but /home/input/pulse_sequence.in does not exist")
        set_pulse_sequence(LaserCircuit1, "./pulse_sequence")
        LaserCircuit1.run_circuit()


if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''
    main(sys.argv)
