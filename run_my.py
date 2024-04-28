import sys
from get_my_inputs import *
from typing import IO 


def initialise_circuit() -> LaserCircuit:
    #for parsing size of the board 

    print("Creating circuit board...")
    while True:
        try:
            tup = parse_size(input("> "))
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
            curr_emitter =  parse_emitter(curr_input)
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
            curr_receiver =  parse_receiver(curr_input)
            building_Circuit.add_receiver(curr_receiver)
            j += 1
        except (TypeError, ValueError) as e2:
            print(e2)
    print(f"{j} receiver(s) added.\n")
    
    return building_Circuit
    

def is_run_my_circuit_enabled(args: list[str]) -> None:
    i = 0
    while i < len(args):
        if args[i] == "-RUN-MY-CIRCUIT":
            return True
        i += 1
    return False

#change file to IO because of Error
def set_pulse_sequence(circuit: LaserCircuit, pulse_file: IO) -> None:
    f = open(pulse_file, "r")
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
            symbol, frequency, direction = parse_pulse_sequence(line)
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
            i += 1
            

def main():
    """
    The main function takes in one argument args which is the command line arguments of the program.
    For now, you can ignore this. 
    This function for now will simply just call initialise_circuit, get the LaserCircuit instance and use its methods to print the board. 
    It should be the shortest function in this module!
    """
    LaserCircuit1 = initialise_circuit()
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
main()