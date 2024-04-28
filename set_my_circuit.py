# import sorter
# from typing import file 
class Photon:


    def __init__(self, x: int, y: int, frequency: int, direction: str):
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Initialises a Photon instance given an x and y position, as well as a
        frequency and direction. symbol is '.' and absorbed is False by
        default.

        symbol:    str  - the symbol of this photon ('.')
        x:         int  - x position of this photon
        y:         int  - x position of this photon
        frequency: int  - the frequency (THz) of this photon
        direction: str  - the direction in which this photon will travel 
                          ('N', 'E', 'S' or 'W')
        absorbed:  bool - whether or not this photon has been absorbed

        Parameters
        ----------
        x         - the x position to set this photon to
        y         - the y position to set this photon to
        frequency - the frequency to set this photon to
        direction - the direction to set this photon to
        '''
        self.symbol = '.'
        self.x = x
        self.y = y
        # self.component_type = "emitter"
        self.frequency = frequency
        self.direction = direction
        self.absorbed = False


    def move(self, board_width: int, board_height: int) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Updates this photon's position to move one unit based on its direction.
        Do not move the photon if it has been absorbed.

        After moving the photon, if it is out-of-bounds based on the board_width
        and board_height given, you will need to update this photon to be 
        absorbed and set its position back so it's not out-of-bounds.

        Parameters
        ----------
        board_width  - width of circuit board 
        board_height - height of circuit board
        
        ------>board_width
        |
        |
        |
        v
        board_width
        '''
        print(f"{self.get_x()}, {self.get_y()}request move {self.get_direction()}")
        if not self.is_absorbed():
            if self.get_direction() == 'N':
                if self.y > 0:
                    self.y -= 1
                else:
                    self.got_absorbed()
            elif self.get_direction() == 'E':
                if self.x < board_width - 1:    
                    self.x += 1
                else:
                    self.got_absorbed()
            elif self.get_direction() == 'S':
                if self.y < board_height - 1:
                    self.y += 1
                else:
                    self.got_absorbed()
            elif self.get_direction() == 'W':
                if self.x > 0:
                    self.x -= 1
                else:
                    self.got_absorbed()
            print(f"{self.get_x()}, {self.get_y()}request move {self.get_direction()} successfull")

    # def interact_with_component(self, component: Emitter | Receiver | Mirror, timestamp: int) -> None:
    def interact_with_component(self, component: object , timestamp: int) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Handles this photon interacting with the passed in component where
        timestamp is when the photon collided with component. This method
        should return out early if the photon has already been absorbed.

        - If component is an emitter, nothing happens.
        - If component is a receiver, the receiver absorbs this photon and
          stores its energy.
        - If component is a mirror, the mirror reflects it off its surface.
        
        Parameters
        ----------
        component - the component to interact with, being an Emitter, Receiver 
                    or Mirror 
        timestamp - the time in nanoseconds when the photon collided with the
                    component

        Note
        ----
        If you need to query the type of component, use the component_type
        attribute. You cannot import the classes in this module due to
        circular dependencies.

        Example:
        >>> component.get_component_type()
        'emitter'
        '''
        if type(component.get_component_type()) == Emitter:
            return None
        elif type(component.get_component_type()) == Receiver:
            self.got_absorbed()
            component.absorb_photon(self, timestamp)
        # elif type(component.get_component_type()) == Mirror:
        #     print("reflect")

            

    def got_absorbed(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Updates the absorbed attribute to represent an absorption.'''
        self.absorbed = True


    def is_absorbed(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns absorbed.'''
        return self.absorbed


    def set_direction(self, direction: str) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Sets the direction attribute of this photon. If the direction passed
        in is not 'N', 'E', 'S' or 'W', it does not set it.

        Parameters
        ----------
        direction - the new direction to set for this photon
        '''
        if direction == ('N' or 'E' or 'S' or 'W'):
            self.direction = direction

    def get_direction(self) -> str:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns direction.'''
        return self.direction

        
    def get_frequency(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns frequency.'''
        return self.frequency


    def get_symbol(self) -> str:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns symbol.'''
        return self.symbol

    
    def get_x(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns x.'''
        return self.x


    def get_y(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns y.'''
        return self.y 
class Emitter:
    def __init__(self, symbol: str, x: int, y: int):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.component_type = "emitter"
        self.frequency = 0
        self.direction = None
        self.pulse_sequence_set = False

    def get_component_type(self) -> str:
        return self.component_type
    
    def get_symbol(self) -> str:
        return self.symbol
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    # def emit_photon(self) -> Photon:
    # NameError: name 'Photon' is not defined 
    # how to do with this???
    def emit_photon(self):
        new_photon = Photon(self.get_x(), self.get_y(), self.frequency, self.direction)
        return new_photon
    
    def __str__(self) -> str:
        format_str = f"{self.get_symbol()}: {self.get_frequency()}THz, {self.get_direction()}"
        return format_str
        
        
    def set_pulse_sequence(self, frequency: int, direction: str) -> None:
        if frequency > 0 and (direction == 'N' or direction == 'E' or direction == 'S' or direction == 'W'):
            self.direction = direction
            self.frequency = frequency
            # print(f"set {self.direction}")
            # print(f"set {self.frequency}")
        return None
    
    def is_pulse_sequence_set(self) -> bool:
        if self.direction == None and self.frequency == 0:
            return False
        else:
            return True
            
    def get_frequency(self) -> int:
        return self.frequency
    
    def get_direction(self) -> str:
        return self.direction
class Receiver:
    def __init__(self, symbol: str, x: int, y: int):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.component_type = "receiver"
        self.total_energy = 0
        self.photons_absorbed = 0
        self.activated = False
        self.activation_time = 0

    def get_component_type(self) -> str:
        return self.component_type
    
    def get_symbol(self) -> str:
        return self.symbol
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y

    def convert_frequency_to_energy(frequency: int) -> float:
        # h = 6.62607015 * 10 ** (-34)
        # E = h * frequency * 10 ** (12)
        # eV = E / (1.60217662 * 10 ** (-19))
        # return round(eV, 2)
    
        # define our constants for the formulae
        PLANCKS_CONSTANT = 6.62607015 * 10**-34
        THZ_TO_HZ = 10**12
        JOULES_TO_EV = 1.60217662*10**-19

        # calculate the joules then convert to electronvolts
        joules = PLANCKS_CONSTANT * frequency * THZ_TO_HZ
        electronvolts = joules / JOULES_TO_EV
        return round(electronvolts, 2)
    
    def absorb_photon(self, photon: Photon, timestamp: int) -> None:
        print(photon.get_frequency())
        print(type(photon.get_frequency()))
        # photon_energy =  self.convert_frequency_to_energy(photon.get_frequency())
        photon_energy =  Receiver.convert_frequency_to_energy(photon.get_frequency())
        # photon_energy =  self.convert_frequency_to_energy(100)
        self.total_energy += photon_energy
        photon.got_absorbed()
        self.photons_absorbed += 1
        if self.photons_absorbed == 1:
            self.activated = True
            self.activation_time = timestamp


    def is_activated(self) -> bool:
        if self.activated:
            return True
        else: 
            return False
    
    def get_total_energy(self) -> float:
        return self.total_energy
    
    def get_activation_time(self) -> int:
        return self.activation_time
    
    def __str__(self) -> str:
        format_str = f"{self.get_symbol()}: {self.get_total_energy()}eV ({self.photons_absorbed}) {self.get_total_energy()}"
        return format_str
class BoardDisplayer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = self.create_board()
        self.component_type = "receiver"

    def create_board(self) -> list[list[str]]:
        i = 0
        board = []
        while i < self.height:
            row = []
            j = 0
            while j < self.width:
                row.append(' ')
                j += 1
            board.append(row)
            i += 1#行列搞反了
        return board
    # def add_component_to_board(self, component: Emitter | Receiver | Mirror) -> None:
    def add_component_to_board(self, component: Emitter | Receiver ) -> None:
        self.board[component.get_y()][component.get_x()] = component.get_symbol()


    def print_board(self) -> None:
        boundary = "+" + self.width * "-" +"+"
        print(boundary)
        i = 0
        while i < self.height:
            j = 0
            print("|", end="")
            while j < self.width:
                print(f"{self.board[i][j]}", end="")
                j += 1
            i += 1
            print("|")
        print(boundary)

    def add_photon_to_board(self, photon: Photon) -> None:
        if self.board[photon.get_y()][photon.get_x()] == " ":
            self.board[photon.get_y()][photon.get_x()] = "."
class LaserCircuit :
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.emitters: list[Emitter] = []
        self.receivers: list[Receiver] = []
        self.photons: list[Photon] = []
        # self.mirrors: list[Mirror] = []
        self.board_displayer = BoardDisplayer(width, height)
        self.clock = 0

    def print_board(self) -> None:
        # BoardDisplayer.print_board()
        self.board_displayer.print_board()

    # def get_collided_emitter(entity: Emitter | Receiver | Photon | Mirror) -> Emitter | None :
    def get_collided_emitter(entity: Emitter | Receiver ) -> Emitter | None :
        
        return entity
    
    # def get_collided_receiver(entity: Emitter | Receiver | Photon | Mirror) -> Receiver | None :
    def get_collided_receiver(entity: Emitter | Receiver ) -> Receiver | None :
        # i = 0
        # while i < len(self.receivers):
        #     if self.receivers[i].get_x() == entity.get_x() and \
        #         self.receivers[i].get_y() == entity.get_y():
        #         return self.receivers[i]
        #     i += 1
        return entity

    
    def add_emitter(self, emitter: Emitter) -> bool:
        if type(emitter) != Emitter:
            return False
        else:
            # print(emitter)
            # print(emitter.get_x())
            # print(type(emitter.get_x()))
            # print(self.width)
            if emitter.get_x() > self.width - 1  or emitter.get_y() > self.height - 1:
                raise ValueError(f"Error: position ({emitter.get_x()}, {emitter.get_y()}) is out-of-bounds of {self.width}x{self.height} circuit board.")
                return False
            # if LaserCircuit.get_collided_emitter(emitter):
            #     raise ValueError(f"Error: position ({emitter.get_x()}, {emitter.get_y()}) is already taken by emitter '{LaserCircuit.get_collided_emitter(emitter).get_symbol()}'.")
            #     return False

            i = 0
            while i < len(self.emitters):
                if emitter.get_x() == self.emitters[i].get_x() and emitter.get_y() == self.emitters[i].get_y():
                    raise ValueError(f"Error: position ({emitter.get_x()}, {emitter.get_y()}) is already taken by emitter '{LaserCircuit.get_collided_emitter(self.emitters[i]).get_symbol()}'.")
                    return False
                if emitter.get_symbol() == self.emitters[i].get_symbol():
                    raise ValueError(f"Error: symbol '{emitter.get_symbol()}' is already taken.")
                    return False
                i += 1
            ##all the check passed
            self.emitters.append(emitter)
            # print(emitter)
            self.emitters.sort(key=lambda Emitter: Emitter.symbol)
            # people.sort(key=lambda person: person.age)
            # print(emitter)
            self.board_displayer.add_component_to_board(emitter)
            return True
                

    def get_emitters(self) -> list[Emitter]:
        return self.emitters
    


    def add_receiver(self, receiver: Receiver) -> bool:
        if type(receiver) != Receiver:
            return False
        else:
            if receiver.get_x() > self.width - 1 or receiver.get_y() > self.height - 1:
                raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is out-of-bounds of {self.width}x{self.height} circuit board.")
                return False
            # if LaserCircuit.get_collided_receiver(receiver):
            #     raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by receiver '{LaserCircuit.get_collided_receiver(receiver).get_symbol()}'.")
            #     return False
            j = 0
            while j < len(self.emitters):
                if receiver.get_x() == self.emitters[j].get_x() and receiver.get_y() == self.emitters[j].get_y():
                    raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by emitter '{LaserCircuit.get_collided_emitter(self.emitters[j]).get_symbol()}'.")
                    return False
                j += 1
            
            i = 0
            while i < len(self.receivers):

                if receiver.get_x() == self.receivers[i].get_x() and receiver.get_y() == self.receivers[i].get_y():
                    raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by receiver '{LaserCircuit.get_collided_receiver(self.receivers[i]).get_symbol()}'.")
                    return False
                if receiver.get_symbol() == self.receivers[i].get_symbol():
                    raise ValueError(f"Error: symbol '{receiver.get_symbol()}' is already taken.")
                    return False
                i += 1
            ##all the check passed
            self.receivers.append(receiver)
            self.receivers.sort(key=lambda Receiver: Receiver.symbol)
            # self.receivers.sort()
            receiver.symbol = receiver.symbol[1:]
            self.board_displayer.add_component_to_board(receiver)
            return True
                
    def get_receivers(self) -> list[Receiver]:
        return self.receivers
    

    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height

    def add_photon(self, photon: Photon) -> bool:
        if type(photon) == Photon:
            self.photons.append(photon)
            return True
        else:
            return False

    def get_photons(self) -> list[Photon]:
        return self.photons
    
    # Let's take the board above and say we call the add_photon_to_board 5 times. In the first call, the photon passed in has position(0, 1), the same position as the emitter A. In the second call, the photon passed in has position (1, 1), and so on, all the way up to position (4, 1), which has the same position as the receiver R0.. The board attribute will now look like this.
    def emit_photons(self) -> None:
        i = 0
        while i < len(self.get_emitters()):
            new_photon = Photon(self.get_emitters()[i].get_x(), \
                                   self.get_emitters()[i].get_y(), \
                                   self.get_emitters()[i].get_frequency(), \
                                   self.get_emitters()[i].get_direction() )
            self.add_photon(new_photon)
            self.board_displayer.add_photon_to_board(new_photon)
            i += 1

    def is_finished(self) -> bool:
        i = 0
        while i < len(self.get_photons()):
            if not self.get_photons()[i].is_absorbed():
                return False
            i += 1
        return True

    def print_emit_photons(self) -> None:
        start = "0ns: Emitting photons."
        print(start)

        i = 0
        print(f"len(self.get_emitters()): {len(self.get_emitters())}")
        while i < len(self.get_emitters()):
            if self.get_emitters()[i].get_direction() == "N":
                full_direction = "North"
            elif self.get_emitters()[i].get_direction() == "S":
                full_direction = "South"
            elif self.get_emitters()[i].get_direction() == "W":
                full_direction = "West"
            elif self.get_emitters()[i].get_direction() == "E":
                full_direction = "East"
            output = f"{self.get_emitters()[i].get_symbol()}: {self.get_emitters()[i].get_frequency()}THz, {full_direction}"
            print(output)
            # with open("/home/output/emit_photons.out", "a") as file:
            with open("./emit_photons_out", "a") as file:
                file.write(output)
                file.close()
            i += 1

    def print_activation_times(self) -> None:

        self.receivers.sort(key=lambda Receiver: Receiver.activation_time)

        i = 0
        while i < len(self.get_receivers()):
            output = f"R{self.get_receivers()[i].get_symbol()}: {self.get_receivers()[i].get_activation_time()}ns"
            print(output)
            # with open("/home/output/activation_times.out", "a") as file:
            with open("./activation_times", "a") as file:
                file.write(output)
                file.close()
            i += 1

    def print_total_energy_absorbed(self) -> None:
        #sorter
        i = 0
        while i < len(self.get_receivers()):
            output = f"R{self.get_receivers()[i].get_symbol()}: {self.get_receivers()[i].get_total_energy()}eV ({self.get_receivers()[i].photons_absorbed})"
            print(output)
            # with open("/home/output/total_energy.out", "a") as file:
            with open("./total_energy_out", "a") as file:
                file.write(output)
                file.close()
            i += 1

    # def get_collided_component(self, photon: Photon) -> Emitter | Receiver | Mirror | None
    def get_collided_component(self, photon: Photon) -> Emitter | Receiver |  None:
        i = 0
        while i < len(self.get_emitters()):
            if photon.get_x() == self.get_emitters()[i].get_x() and \
                photon.get_y() == self.get_emitters()[i].get_y():
                return self.get_emitters()[i]
            i += 1

        j = 0
        while j < len(self.get_receivers()):
            if photon.get_x() == self.get_receivers()[j].get_x() and \
                photon.get_y() == self.get_receivers()[j].get_y():
                return self.get_receivers()[j]
            j += 1
        
        k = 0
        while k < len(self.get_photons()):
            if photon.get_x() == self.get_photons()[k].get_x() and \
                photon.get_y() == self.get_photons()[k].get_y():
                return self.get_photons()[k]
            k += 1
        
        return None
    
    def tick(self) -> None:
        if self.is_finished():
            return None
        i = 0
        while i < len(self.get_photons()):
            if not self.get_photons()[i].is_absorbed():
                self.get_photons()[i].move(self.get_width(), self.get_height())
                print(f"self.get_photons()[i]:{self.get_photons()[i]} {self.get_photons()[i].get_x()} {self.get_photons()[i].get_y()} ")
                self.board_displayer.add_photon_to_board(self.get_photons()[i])
                collided_component = self.get_collided_component(self.get_photons()[i])
                print(collided_component)
                if type(collided_component) == Receiver:
                    collided_component.absorb_photon(self.get_photons()[i], self.clock)
                    
                # ???
                # If the photon collides with a component, interact with it (if applicable).
                # collided_component.in
            i += 1
        self.clock += 1


    def run_circuit(self) -> None:
        print("========================\n   RUNNING CIRCUIT...\n========================")
        self.emit_photons()
        self.print_emit_photons()
        #不按照案例来，改成finish的时候break出来
        # while self.is_finished() == False:
        i = 0
        while True:
        # while i < 5:
            self.tick()
            if self.clock % 5 == 0 or self.is_finished():
                #store the rec_activated
                rec_activated = []
                i = 0
                while i < len(self.get_receivers()):
                    if self.get_receivers()[i].is_activated():
                        rec_activated.append(self.get_receivers()[i].get_symbol())
                    i += 1
                print(f"{self.clock}ns: {len(rec_activated)}/{len(self.get_receivers())} receiver(s) activated.")
                self.print_board()
                if self.is_finished():
                    break

        self.print_activation_times()
        self.print_total_energy_absorbed()
        print("========================\n   RUNNING FINISHED!\n========================")