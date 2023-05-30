#!usr/bin/env python3
""" Developed for the bus drivers of CodeTown by A.Robertson.
    Keeps track of passengers boarding/leaving bus and gives
    a final result of 'Happy Customers' vs 'Unhappy Customers'
    as well as a ratio to two decimal points.
    Used to help facilitate the decision-making process of the
    Mayor of CodeTown in changing school hours.
    Saves relevant information in a text file for later viewing.
    """

information = {  # holds all the information needed for the final result
    'Bus Route': 0,
    'Stop Amount': 0,
    'Happy Customers': 0,
    'Unhappy Customers': 0,
    'Ratio': '0.00'
}

# global variables to help certain functions keep track of passengers
on_bus = 0
left_behind = 0


def ratio(x, y):
    """ Find the ratio of 2 numbers to 2 decimal points

        Key Arguments:
            x -- First term for division
            y -- Second term for division

        Coverts both key arguments to floats, and then
        performs a division. It then stores the result
        as a string, formatted to have 2 decimal places.
        Stores the string in the dictionary 'information'
        under key 'Ratio'.
        If the result is 0, returns 0.00.
        """
    try:
        val1 = float(x)
        val2 = float(y)
        result = val1 / val2
        result_str = f'{result:.{2}f}'  # Formats string to have 2 decimal places
    except ZeroDivisionError:
        return 0.00

    information['Ratio'] = result_str


def ask_route():
    """ Asks the driver for the route number.

        Accepts only positive integers. Stores the information
        in the dictionary 'information' under key 'Route Number'.
     """
    while True:
        try:
            route_no = int(input("Please enter your bus route number: "))
            print('You have entered: ', route_no)
            if route_no < 0:
                raise ValueError
            information['Bus Route'] = route_no
            break
        except (ValueError, TypeError):
            print('Invalid input. Please use a positive integer. Try again. ')
            continue


def ask_stops():
    """Asks the driver how many stops they have on their route.

       Accepts only positive integers from their input.
       Stores the input in the dictionary 'information'
       under key 'Stop Amount'.
       """
    while True:
        try:
            stop_amt = int(input('how many stops are on your route?: '))
            print('You have entered: ', stop_amt)
            if stop_amt < 2:
                raise TypeError
            information['Stop Amount'] = stop_amt
            break
        except ValueError:  # user entered "a" etc.
            print('Invalid input. Please use a positive integer. Try again.')
            continue
        except TypeError:  # if less than 2 stops
            print('Invalid input. There must be at least 2 stops on your route. Try again. ')
            continue


def passenger_count():
    """ Track passengers per stop.

        Keeps track of the passengers getting off/on
        at each stop, storing the results of each stop
        in the dictionary 'information'.
        As passengers get on the bus, increments key
        'Happy Passengers'. Checks how many passengers
        are on the bus and if the bus is full, it subtracts
        the overflow amount from key 'Happy Passengers'
        and instead increments key 'Unhappy Passengers'.
        Reports to the user the current number of passengers
        on the bus, and the value they entered when asked for
        input.
        """
    global on_bus, left_behind
    for i in range(1, information.get('Stop Amount')):
        while True:
            try:
                if i > 1:  # Becomes True when we reach stop 2
                    while True:
                        try:
                            psg_off = int(input('How many passengers got off at stop ' + str(i) + "?: "))
                            print('you have entered: ', psg_off)

                            if psg_off > on_bus:
                                raise ValueError
                            if psg_off < 0:
                                raise TypeError

                            on_bus -= psg_off
                            print(on_bus, 'passengers on bus currently')

                            break

                        except ValueError:  # More passengers getting off bus than there are currently on bus
                            print('Invalid input, there are only', str(on_bus), 'passengers on the bus. Try again. ')
                            continue
                        except TypeError:  # non-int input or negative integer input
                            print('Invalid input, please enter a positive integer. Try again. ')
                            continue

                psg_on = int(input("How many passengers were waiting for the bus at stop " + str(i) + "?: "))
                print('You have entered: ', psg_on)

                if psg_on < 0:
                    raise ValueError

                on_bus += psg_on

                if on_bus > 47:  # bus is full, increment 'Unhappy Passengers'
                    print("No more customers can fit on the bus! ")
                    for e in range(47, on_bus):
                        on_bus -= 1
                        left_behind = e - 47
                        information['Unhappy Customers'] += 1
                        information['Happy Customers'] -= 1  # Take from key as all passengers boarding increments key
                    print(str(left_behind + 1), ' customers left behind!')

                print(on_bus, 'passengers on bus currently.')

                information['Happy Customers'] = int(information.get('Happy Customers')) + psg_on

                break
            except ValueError:
                print('Invalid input. You must use a positive integer. Please try again. ')
                continue


def final_stop():
    """ Facilitates the final stop on the bus' journey.

        Once the initial for loop in passenger_count() ends,
        prints out how many passengers left the bus.
        Doesn't need to modify any variables as that behaviour
        is handled by passenger_count()
        """
    global on_bus
    print('You have arrived at your final stop.')
    print(on_bus, 'passengers left the bus.')


def print_results():
    """ Print results to terminal and saves them for later viewing

        Once the program has tallied up all the results, it prints
        out everything in the dictionary 'information' to the
        terminal, and then saves the contents of 'information' to
        a text file for later viewing
        """
    print('Printing results...')
    print("Bus Route: ", information['Bus Route'])
    print("Amount of stops: ", information['Stop Amount'])
    print("Happy customers: ", information['Happy Customers'])
    print("Unhappy customers: ", information['Unhappy Customers'])
    print("Ratio of happy to unhappy customers: ", information['Ratio'])
    f = open("Results.txt", "w")  # Create new .txt file
    f.write(str(information))
    f.close()


if __name__ == '__main__':
    ask_route()
    ask_stops()
    passenger_count()
    final_stop()
    ratio(information['Happy Customers'], information['Unhappy Customers'])
    print_results()
