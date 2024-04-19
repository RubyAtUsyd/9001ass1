"""
def add_receiver(self, receiver: receiver) -> bool:
        if type(receiver) != receiver:
            return False
        else:
                if receiver.get_x() > self.width or receiver.get_y() > self.height:
                    raise ValueError(f"Error: position ({})")
                    return False
                if LaserCircuit.get_collided_receiver(receiver):
                    raise ValueError("Argument is not int or float!")
                    return False
                i = 0
                while i < len(self.receivers):
                    if receiver.get_symbol() == self.receivers[i].get_symbol():
                        raise ValueError("taken")
                        return False
                    i += 1
                ##all the check passed
                self.receivers = self.receivers.append(receiver)
                self.receivers.sort()
                BoardDisplayer.add_component_to_board(receiver)
                return True
                

        


    def get_receivers(self) -> list[receiver]:
        return self.receivers
"""