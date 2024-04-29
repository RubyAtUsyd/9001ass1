import sorter
from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from board_displayer import BoardDisplayer

'''
Name:   Ruby Liang
SID:    540180464
Unikey: blia0673

LaserCircuit - Responsible for storing all the components of the circuit and
handling the computation of running the circuit. It's responsible for delegating 
tasks to the specific components e.g. making each emitter emit a photon, getting 
each photon to move and interact with components, etc. In general, this class is
responsible for handling any task related to the circuit.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class LaserCircuit:


    def __init__(self, width: int, height: int):
        '''        
        Initialise a LaserCircuit instance given a width and height. All 
        lists of components and photons are empty by default.
        board_displayer is initialised to a BoardDisplayer instance. clock is
        0 by default.

        emitters:        list[Emitter]  - all emitters in this circuit
        receivers:       list[Receiver] - all receivers in this circuit
        photons:         list[Photon]   - all photons in this circuit
        mirrors:         list[Mirror]   - all mirrors in this circuit
        width:           int            - the width of this circuit board
        height:          int            - the height of this circuit board
        board_displayer: BoardDisplayer - helper class for storing and 
                                          displaying the circuit board
        clock:           int            - a clock keeping track of how many 
                                          nanoseconds this circuit has run for

        Parameters
        ----------
        width  - the width to set this circuit board to
        height - the width to set this circuit board to
        '''
        self.width = width
        self.height = height
        self.emitters: list[Emitter] = []
        self.receivers: list[Receiver] = []
        self.photons: list[Photon] = []
        self.mirrors: list[Mirror] = []
        self.board_displayer = BoardDisplayer(width, height)
        self.clock = 0


    def emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Gets each emitter in this circuit's list of emitters to emit a photon.
        The photons emitted should be added to this circuit's photons list.
        '''
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
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns whether or not this circuit has finished running. The
        circuit is finished running if every photon in the circuit has been
        absorbed.

        Returns
        -------
        True if the circuit has finished running or not, else False.
        '''
        i = 0
        while i < len(self.get_photons()):
            if not self.get_photons()[i].is_absorbed():
                return False
            i += 1
        return True


    def print_emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for each emitter emitting a photon.
        
        It will also need to write the output into a
        /home/output/emit_photons.out output file. 
        
        You can assume the /home/output/ path exists.
        '''
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
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the activation times for each receiver, sorted
        by activation time in ascending order. Any receivers that have not
        been activated should not be included.
        
        It will also need to write the output into a
        /home/output/activation_times.out output file.

        You can assume the /home/output/ path exists.
        '''
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


    def print_total_energy(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the total energy absorbed for each receiver,
        sorted by total energy absorbed in descending order. Any receivers
        that have not been activated should not be included.
        
        It will also need to write the output into a
        /home/output/total_energy_absorbed.out output file.

        You can assume the /home/output/ path exists.
        '''
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

    
    def print_board(self) -> None:
        '''Calls the print_board method in board_displayer.'''
        self.board_displayer.print_board()


    def get_collided_emitter(self, entity: Emitter | Receiver | Photon | Mirror) -> Emitter | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another emitter in the 
        circuit. 

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no emitter occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        An emitter if it has the same position as entity, else None.
        '''
        i = 0
        while i < len(self.emitters):
            if self.emitters[i].get_x() == entity.get_x() and \
                self.emitters[i].get_y() == entity.get_y():
                return self.emitters[i]
            i += 1
        return None


    def get_collided_receiver(self, entity: Emitter | Receiver | Photon | Mirror) -> Receiver | None:
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another receiver in the 
        circuit. 

        If it does, return the receiver already in the entity's position.
        Else, return None, indicating there is no receiver occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A receiver if it has the same position as entity, else None.
        '''
        i = 0
        while i < len(self.receivers):
            if self.receivers[i].get_x() == entity.get_x() and \
                self.receivers[i].get_y() == entity.get_y():
                return self.receivers[i]
            i += 1
        return None


    def get_collided_mirror(self, entity: Emitter | Receiver | Photon | Mirror) -> Mirror | None:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another mirror in the 
        circuit. 

        If it does, return the mirror already in the entity's position.
        Else, return None, indicating there is no mirror occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A mirror if it has the same position as entity, else None.
        '''
        i = 0
        while i < len(self.mirrors):
            if self.mirrors[i].get_x() == entity.get_x() and \
                self.mirrors[i].get_y() == entity.get_y():
                return self.mirrors[i]
            i += 1
        return None


    def get_collided_component(self, photon: Photon) -> Emitter | Receiver | Mirror | None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Given a photon, returns the component it has collided with (if any).
        A collision occurs if the positions of photon and the component are
        the same.

        Parameters
        ----------
        photon - a photon to check for collision with the circuit's components

        Returns
        -------
        If the photon collided with a component, return that component.
        Else, return None.

        Hint
        ----
        Use the three collision methods above to handle this.
        '''
        if self.get_collided_emitter(photon):
            return self.get_collided_emitter(photon)

        if self.get_collided_receiver(photon):
            return self.get_collided_receiver(photon)
        
        if self.get_collided_mirror(photon):
            return self.get_collided_mirror(photon)

        return None


    def tick(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs a single nanosecond (tick) of this circuit. If the circuit has
        already finished, this method should return out early.
        
        Otherwise, for each photon that has not been absorbed, this method is
        responsible for moving it, updating the board to show its new position
        and checking if it collided with a component (and handling it if did
        occur). At the end, we then increment clock.
        '''
        
        if self.is_finished():
            return None
        self.clock += 1
        i = 0
        while i < len(self.get_photons()):
            if not self.get_photons()[i].is_absorbed():
                self.get_photons()[i].move(self.get_width(), self.get_height())
                print(f"self.get_photons()[i]:{self.get_photons()[i]} {self.get_photons()[i].get_x()} {self.get_photons()[i].get_y()} ")
                self.board_displayer.add_photon_to_board(self.get_photons()[i])
                #if collided
                collided_component = self.get_collided_component(self.get_photons()[i])
                print(f"collided_component{collided_component}")
                if collided_component:
                    print(f"self.get_photons()[i].get_direction(){self.get_photons()[i].get_direction()}")
                    self.get_photons()[i].interact_with_component(collided_component, self.clock)
                    print(f"self.get_photons()[i].get_direction(){self.get_photons()[i].get_direction()}")
            i += 1
        # self.clock += 1


    def run_circuit(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs the entire circuit from start to finish. This involves getting
        each emitter to emit a photon, and continuously running tick until the
        circuit is finished running. All output in regards of running the 
        circuit should be contained in this method.
        '''
        print("========================\n   RUNNING CIRCUIT...\n========================")
        self.emit_photons()
        self.print_emit_photons()
        #不按照案例来，改成finish的时候break出来
        # while self.is_finished() == False:
        j = 0
        while True:
        # while j < 5:
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
            # j += 1
        self.print_activation_times()
        self.print_total_energy()
        print("========================\n   RUNNING FINISHED!\n========================")


    
    def add_emitter(self, emitter: Emitter) -> bool:
        '''
        If emitter is not an Emitter instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The emitter's position is within the bounds of the circuit.
          2)  The emitter's position is not already taken by another emitter in
              the circuit.
          3)  The emitter's symbol is not already taken by another emitter in 
              the circuit.
          
        If at any point a check is not passed, an error message is printed
        stating the causeof the error and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur:
          1)  emitter is added in the circuit's list of emitters. emitter
              needs to be added such that the list of emitters remains sorted
              in alphabetical order by the emitter's symbol. You can assume the
              list of emitters is already sorted before you add the emitter.
          2)  emitter's symbol is added into board_displayer.
          3)  The method returns True.   

        Parameters
        ----------
        emitter - the emitter to add into this circuit's list of emitters

        Returns
        ----------
        Returns true if all checks are passed and the emitter is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter method to check for position collision.
        You will need to find your own way to check for symbol collisions
        with other emitters.
        '''
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
            if self.get_collided_emitter(emitter):
                raise ValueError(f"Error: position ({emitter.get_x()}, {emitter.get_y()}) is already taken by emitter '{self.get_collided_emitter(emitter).get_symbol()}'.")
                return False

            i = 0
            while i < len(self.emitters):
                # if emitter.get_x() == self.emitters[i].get_x() and emitter.get_y() == self.emitters[i].get_y():
                #     raise ValueError(f"Error: position ({emitter.get_x()}, {emitter.get_y()}) is already taken by emitter '{LaserCircuit.get_collided_emitter(self.emitters[i]).get_symbol()}'.")
                #     return False
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
        '''Returns emitters.'''
        return self.emitters

    
    def add_receiver(self, receiver: Receiver) -> bool:
        '''
        If receiver is not a Receiver instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The receiver's position is within the bounds of the circuit.
          2)  The receiver's position is not already taken by another emitter
              or receiver in the circuit.
          3)  The receiver's symbol is not already taken by another receiver in
              the circuit. 
             
        If at any point a check is not passed, an error message is printed stating
        the cause of the error and returns False, skipping any further checks. If 
        all checks pass, then the following needs to occur:
          1)  receiver is added in the circuit's list of receivers. receiver
              needs to be added such that the list of receivers  remains sorted
              in alphabetical order by the receiver's symbol. You can assume the
              list of receivers is already sorted before you add the receiver. 
          2)  receiver's symbol is added into board_displayer.
          3)  The method returns True.

        Parameters
        ----------
        receiver - the receiver to add into this circuit's list of receivers

        Returns
        ----------
        Returns true if all checks are passed and the receiver is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter and get_collided_receiver methods to
        check for position collisions.
        You will need to find your own way to check for symbol collisions
        with other receivers.
        '''
        if type(receiver) != Receiver:
            return False
        else:
            if receiver.get_x() > self.width - 1 or receiver.get_y() > self.height - 1:
                raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is out-of-bounds of {self.width}x{self.height} circuit board.")
                return False
            
            if self.get_collided_emitter(receiver):
                raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by emitter '{self.get_collided_emitter(receiver).get_symbol()}'.")
                return False
            if self.get_collided_receiver(receiver):
                raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by receiver '{self.get_collided_receiver(receiver).get_symbol()}'.")
                return False
            # j = 0
            # while j < len(self.emitters):
            #     if receiver.get_x() == self.emitters[j].get_x() and receiver.get_y() == self.emitters[j].get_y():
            #         raise ValueError(f"Error: position ({receiver.get_x()}, {receiver.get_y()}) is already taken by emitter '{LaserCircuit.get_collided_emitter(self.emitters[j]).get_symbol()}'.")
            #         return False
            #     j += 1
            
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
        '''Returns receivers.'''
        return self.receivers


    def add_photon(self, photon: Photon) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        If the photon passed in is not a Photon instance, it does not add it in
        and returns False. Else, it adds photon in this circuit's list of
        photons and returns True.

        Parameters
        ----------
        photon - the photon to add into this circuit's list of photons

        Returns
        -------
        Returns True if the photon is added in, else False.
        '''
        if type(photon) == Photon:
            self.photons.append(photon)
            return True
        else:
            return False


    def get_photons(self) -> list[Photon]:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns photons.'''
        return self.photons


    def add_mirror(self, mirror: Mirror) -> bool:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        If mirror is not a Mirror instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The mirror's position is within the bounds of the circuit.
          2)  The mirror's position is not already taken by another emitter, 
              receiver or mirror in the circuit.
             
        If at any point a check is not passed, an error message is printed
        stating the cause of theerror and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur: 
          1)  mirror is added in the circuit's list of mirrors.
          2) mirror's symbol is added into board_displayer.
          3)   The method returns True.

        Parameters
        ----------
        mirror - the mirror to add into this circuit's list of mirrors

        Returns
        ----------
        Returns true if all checks are passed and the mirror is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.
        '''
        if type(mirror) != Mirror:
            return False
        else:
            if mirror.get_x() > self.width - 1 or mirror.get_y() > self.height - 1:
                raise ValueError(f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is out-of-bounds of {self.width}x{self.height} circuit board.")
                return False

            if self.get_collided_emitter(mirror):
                raise ValueError(f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is already taken by emitter '{self.get_collided_emitter(mirror).get_symbol()}'.")
                return False
            if self.get_collided_receiver(mirror):
                raise ValueError(f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is already taken by receiver '{self.get_collided_receiver(mirror).get_symbol()}'.")
                return False
            if self.get_collided_mirror(mirror):
                raise ValueError(f"Error: position ({mirror.get_x()}, {mirror.get_y()}) is already taken by mirror '{self.get_collided_mirror(mirror).get_symbol()}'.")
                return False
            ##all the check passed
            self.mirrors.append(mirror)
            self.mirrors.sort(key=lambda Mirror: Mirror.symbol)
            # self.receivers.sort()
            self.board_displayer.add_component_to_board(mirror)
            return True


    def get_mirrors(self) -> list[Mirror]:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns mirrors.'''
        return self.mirrors

    
    def get_width(self) -> int:
        '''Returns width.'''
        return self.width


    def get_height(self) -> int:
        '''Returns height.'''
        return self.height
