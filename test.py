from laser_circuit import LaserCircuit
from emitter import Emitter

'''
Name:   Xxx Yyy
SID:    XXXXXXXXX
Unikey: xxxxXXXX

This test program checks if the RGB features are implemented correctly. 

The scaffold provides a rough guideline with a function intended for 
testing the implementation of an emitter's colour. 
Modify the scaffold as needed to include
a minimum of 4 test cases as specified in the description.

You are free to add as many test functions as you want. You can also
modify it to take in arguments if required.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''


def test_emitter_colour_change():
    '''
    Test case to verify the correct implementation of photon colours.

    The scaffold provides setting up the following:
    colours - The mapping of frequency ranges to colours.
    circuit - LaserCircuit object, the circuit instance for testing
    emitter - Emitter object, the emitter instance for testing
    '''
    # STEP 1: Set up the Circuit
    #         Prepare for testing emitter colour change
    colours = ...
    circuit = LaserCircuit(4, 3, colours)
    emitter = Emitter("A", 2, 2)
    circuit.add_emitter(emitter)

    # STEP 2 Check if board and its components are set up as assumed
    assert circuit.board_displayer.board[emitter.get_x()][emitter.get_y()] \
        == f'\x1b[4m{emitter.get_symbol()}\x1b[0m'

    # STEP 3: Call tick() 
    # You are free to perform additional actions / multiple ticks if needed
    circuit.tick()

    # STEP 4: Check if emitter's colour is correctly changed
    assert circuit.board_displayer.board[emitter.get_x()][emitter.get_y()] \
        == f'\x1b[38;5;245m{emitter.get_symbol()}\x1b[0m'


if __name__ == '__main__':
    # Run all test functions (test cases)
    # NOTE: Number of parameters/arguments and their types are changeable.
    test_emitter_colour_change()
    # you'll be calling more tests below...

