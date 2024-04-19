from get_my_inputs import *


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
    print(f"{width_i}x{height_i} board created.")
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
    print(f"{i} emitter(s) added.")

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
    print(f"{j} receiver(s) added.")
    
    return building_Circuit
    
def main():
    """
    The main function takes in one argument args which is the command line arguments of the program.
    For now, you can ignore this. 
    This function for now will simply just call initialise_circuit, get the LaserCircuit instance and use its methods to print the board. 
    It should be the shortest function in this module!
    """
    LaserCircuit1 = initialise_circuit()
    LaserCircuit1.print_board()
main()