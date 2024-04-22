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


class Receiver:
    def __init__(self, symbol: str, x: int, y: int):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.component_type = "receiver"
        self.total_energy = 0
        self.photons_absorbed = 0
        self.activation_time = 0

    def get_component_type(self) -> str:
        return self.component_type
    
    def get_symbol(self) -> str:
        return self.symbol
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y

    
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


class LaserCircuit :
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.emitters: list[Emitter] = []
        self.receivers: list[Receiver] = []
        # self.photons: list[Photon] = []
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
        if self.get_direction() == 'N':
            if self.y > 0:
                self.y -= 1
        elif self.get_direction() == 'E':
            if self.x < board_width - 2:    
                self.x += 1
        elif self.get_direction() == 'S':
            if self.y < board_height - 2:
                self.y += 1
        elif self.get_direction() == 'W':
            if self.x > 0:
                self.x -= 1



    def interact_with_component(self, component: Emitter | Receiver | Mirror, timestamp: int) -> None:
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
        elif type(component.get_component_type()) == Mirror:
            print("reflect")

            


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