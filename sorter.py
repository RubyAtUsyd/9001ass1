from emitter import Emitter
from receiver import Receiver

'''
Name:   Xxx Yyy
SID:    XXXXXXXXX
Unikey: xxxxXXXX

sorter - A module that provides sorting functions for you to use.
Since most students taking this course have not done algorithms, you are not
expected to know how to sort. You should have the ability to use our sort
functions to handle it in your program when needed.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def sort_receivers_by_symbol(receivers: list[Receiver]) -> list[Receiver]:
    # this method has already been implemented for you
    '''
    This is a helper function which returns a new list of the same receivers
    passed in, sorted by their symbol in ascending order. This is used to resolve
    ties when sorting by other values.

    Parameters
    ----------
    receivers - a list of receivers

    Returns
    -------
    A new list containing the same receivers, sorted by their symbol in
    ascending order.
    '''
    # copy the receivers objects into a new list so we don't modify the original
    new_list = receivers.copy()

    # perform a bubble sort
    i = 0
    # traverse through all receivers in the list
    while i < len(new_list):
        j = i
        while j < len(new_list):
            # compare the symbols of the two adjacent receivers
            # swap them if the component at the front has a larger symbol
            if new_list[i].get_symbol() > new_list[j].get_symbol():
                # swap the positions of the receivers in the list
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp
            j += 1
            # at this point, all elements from 0 to i is sorted
        i += 1

    return new_list


def sort_receivers_by_activation_time(receivers: list[Receiver]) -> list[Receiver]:
    # this method has already been implemented for you
    '''
    This function returns a new list of the same receivers passed in, sorted by
    their activation time in ascending order. If there's any ties, they are
    then sorted by symbol in asecnding order.

    Parameters
    ----------
    receivers - a list of receivers

    Returns
    -------
    A new list containing the same receivers, sorted by their activation times
    in ascending order, followed by a sorting of their symbol in ascending order.
    '''
    # sort our receivers by symbol to resolve ties
    new_list = sort_receivers_by_symbol(receivers)    

    i = 0
    while i < len(new_list):
        j = i
        while j < len(new_list):
            # compare the activation time of the two adjacent receivers
            # swap them if the receiver at the front has a larger activation time
            if new_list[i].get_activation_time() > new_list[j].get_activation_time():
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp
            j += 1
        i += 1

    return new_list


def sort_receivers_by_total_energy(receivers: list[Receiver]) -> list[Receiver]:
    # this method has already been implemented for you
    '''
    This function returns a new list of the same receivers passed in, sorted by
    their total energy in ascending order. If there's any ties, they are
    then sorted by symbol in asecnding order.

    Parameters
    ----------
    receivers - a list of receivers

    Returns
    -------
    A new list containing the same receivers, sorted by their total energy in
    descending order, followed by a sorting of their symbol in ascending order.
    '''
    # sort our receivers by symbol to resolve ties
    new_list = sort_receivers_by_symbol(receivers)

    i = 0
    while i < len(new_list):
        j = i
        while j < len(new_list):
            # compare the total energy of the two adjacent receivers
            # swap them if the receiver at the front has a smaller total energy
            if new_list[i].get_total_energy() < new_list[j].get_total_energy():
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp
            j += 1
        i += 1

    return new_list
