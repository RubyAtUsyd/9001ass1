from photon import Photon

'''
Name:   Xxx Yyy
SID:    XXXXXXXXX
Unikey: xxxxXXXX

Receiver - A photodetector which absorbs photons and stores its energy. 
When a photon reaches a receiver, the receiver will absorb the photon and
absorb its energy. Once a receiver absorbs a photon, the receiver becomes
activated. An activated receiver can keep absorbing photons.

You are free to add more attributes and methods, as long as you aren't
modifying the existing scaffold.
'''


class Receiver:


    def __init__(self, symbol: str, x: int, y: int):
        '''
        Initialises a Receiver instance with a given symbol, x and y value. 
        component_type is 'receiver', total_energy is 0.0, photons_absorbed is 0, 
        activated is False and activation_time is 0 by default.

        component_type:   str   - represents the type of component ('receiver')
        symbol:           str   - the symbol of this receiver ('R0' to 'R9')
        x:                int   - x position of this receiver 
        y:                int   - y position of this receiver
        total_energy:     float - the total energy (eV) this receiver has absorbed 
                                  from photons
        photons_absorbed: int   - the number of photons this receiver has absorbed
        activated:        bool  - whether this receiver is activated or not       
        activation_time:  int   - the time (ns) in which this receiver was 
                                  activated

        Parameters
        ----------
        symbol - the symbol to set this receiver to
        x      - the x position to set this receiver to
        y      - the y position to set this receiver to       
        '''
        pass


    def convert_frequency_to_energy(frequency: int) -> float:
        # this method has already been implemented for you
        '''
        Converts the given frequency (THz) to energy (eV).
        
        Parameters
        ----------
        frequency - the frequency to convert to energy

        Returns
        -------
        The energy calculated from the frequency.
        '''
        # define our constants for the formulae
        PLANCKS_CONSTANT = 6.62607015 * 10**-34
        THZ_TO_HZ = 10**12
        JOULES_TO_EV = 1.60217662*10**-19

        # calculate the joules then convert to electronvolts
        joules = PLANCKS_CONSTANT * frequency * THZ_TO_HZ
        electronvolts = joules / JOULES_TO_EV
        return electronvolts


    def absorb_photon(self, photon: Photon, timestamp: int) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Absorbs the photon, where timestamp (ns) is when the photon collided
        with this receiver. This method should return out early if the photon
        has already been absorbed. 
        
        Otherwise, this receiver should have total_energy and photons_absorbed
        updated. If this is the first photon absorbed, activated and
        activation_time should also update.
        
        In the end, photon should be updated to be absorbed.   
        
        Parameters
        ----------
        photon    - the photon to absorb for this receiver
        timestamp - the time in nanoseconds when the photon collided with this
                    receiver
        '''
        pass


    def is_activated(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns whether or not this receiver is activated. '''
        pass

    
    def get_total_energy(self) -> float:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns total_energy.'''
        pass


    def get_activation_time(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns activation_time.'''
        pass


    def get_component_type(self) -> str:
        '''Returns component type.'''
        pass


    def get_symbol(self) -> str:
        '''
        Returns the number at the end of the receiver's symbol as a string.

        >>> self.symbol
        'R0'
        >>> self.get_symbol()
        '0'
        '''
        pass


    def get_x(self) -> int:
        '''Returns x.'''
        pass


    def get_y(self) -> int:
        '''Returns y.'''
        pass

    
    def __str__(self) -> str:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns a unique string format of the receiver, containing its symbol,
        frequency and direction.
        
        Returns a string in the format
        <symbol>: <total_energy>eV (<photons_absorbed>) 
        where <total_energy> is rounded to 2dp.

        >>> self.symbol
        'R0'
        >>> self.total_energy
        0.54
        >>> self.photons_absorbed
        2
        >>> print(self)
        R0: 0.54eV (2)
        '''
        pass   