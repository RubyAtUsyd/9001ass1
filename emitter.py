from photon import Photon

'''
Name:   Ruby Liang
SID:    540180464
Unikey: blia0673

Emitter - A laser that emits a photon with a frequency and direction.
The frequency and direction of the photon it emits is determined by the
pulse  sequence.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class Emitter:


    def __init__(self, symbol: str, x: int, y: int):
        '''
        Initialises an Emitter instance given a symbol, x and y value. 
        component_type is 'emitter', frequency is 0 and direction is None by 
        default.

        component_type:     str  - represents the type of component ('emitter')
        symbol:             str  - the symbol of this emitter ('A' to 'J')
        x:                  int  - x position of this emitter
        y:                  int  - y position of this emitter
        frequency:          int  - the frequency (THz) of the photon this emitter 
                                   emits
        direction:          str  - the direction in which the photon this emitter 
                                   emits will travel ('N', 'E', 'S' or 'W')
        pulse_sequence_set: bool - whether or not this emitter has been set by
                                   the pulse sequence

        Parameters
        ----------
        symbol - the symbol to set this emitter to
        x      - the x position to set this emitter to
        y      - the y position to set this emitter to
        '''
        self.symbol = symbol
        self.x = x
        self.y = y
        self.component_type = "emitter"
        self.frequency = 0
        self.direction = None
        self.pulse_sequence_set = False


    def emit_photon(self) -> Photon:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Represents the action of emitting a photon. 
        
        Returns
        ----------
        A photon that inherits this emitter's position, frequency and 
        direction.
        '''
        new_photon = Photon(self.get_x(), self.get_y(), self.frequency, self.direction)
        return new_photon


    def set_pulse_sequence(self, frequency: int, direction: str) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Sets the pulse sequence for this emitter, setting the frequency and
        direction attribute.
        
        The frequency passed in must be greater than zero, and the direction
        passed in must be either 'N', 'E', 'S' or 'W'. If both of these
        conditions are met, update frequency and direction, and update
        pulse_sequence_set, else no change occurs.

        Parameters
        ----------
        frequency - the new frequency to set for this emitter 
        direction - the new direction to set for this emitter      
        '''
        if frequency > 0 and (direction == 'N' or direction == 'E' or direction == 'S' or direction == 'W'):
            self.direction = direction
            self.frequency = frequency
            # print(f"set {self.direction}")
            # print(f"set {self.frequency}")
        return None


    def is_pulse_sequence_set(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns whether or not the pulse sequence for this emitter has been set.'''
        if self.direction == None and self.frequency == 0:
            return False
        else:
            return True
            


    def get_frequency(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns frequency.'''
        return self.frequency


    def get_direction(self) -> str:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns direction.'''
        return self.direction


    def get_component_type(self) -> str:
        '''Returns component type.'''
        return self.component_type


    def get_symbol(self) -> str:
        '''Returns symbol.'''
        return self.symbol

    
    def get_x(self) -> int:
        '''Returns x.'''
        return self.x


    def get_y(self) -> int:
        '''Returns y.'''
        return self.y


    def __str__(self) -> str:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns a unique string format of the emitter, containing its symbol,
        frequency and direction.

        Returns 
        -------
        A string in the format <symbol>: <frequency>THz, <direction> 
        where <direction> is the full word of the direction e.g. if the 
        direction attribute is 'S', <direction> is South.

        Example
        -------
        >>> self.symbol
        'C'
        >>> self.frequency
        256
        >>> self.direction
        'S'
        >>> print(self)
        C: 256THz, South
        '''
        format_str = f"{self.get_symbol()}: {self.get_frequency()}THz, {self.get_direction()}"
        return format_str
