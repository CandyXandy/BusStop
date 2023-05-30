#BusStop


BusStop is a program designed by A. Robertson to help the decision-making process
undergone by the Mayor of CodeTown in deciding whether the current school hours are in-line
with the needs of modern working parents. It does this by collecting data on the bus
routes of CodeTown. In particular, gauging the flow on effects that changing school hours
could have on Public Transport.

This is achieved by gathering data on how the bus routes are currently being utilised.
The data is entered by the bus drivers of said routes and then stored for later viewing.




### Contents:


- Pre-requisites
- How to run
- How to use
- How it works


### Pre-requisites


To run this program you will need a computer that has Python3 installed.<br>
You can find python3 [here](http://python.org/downloads/).
Make sure you install the correct version for your operating system.

### How to run

In your terminal, navigate to the directory where you have BusStop saved.  
Then, type python3 BusStop.py into the terminal   
The program should begin to run.


### How to use:

When the program begins to run, it will display text in the terminal, and ask for input.

>Please enter your bus route number:   

Enter the route number your bus belongs to.   
Take note however, it won't accept any input other than a positive integer.   
Failure to input a positive integer will result in an "Invalid Input" message being displayed.

> Invalid input. Please use a positive integer. Try again.

BusStop will continue to ask until valid input is acquired.     
Once you've entered valid input, BusStop will take note of what you input and store it for later.

Then, BusStop will ask you for the amount of stops on your bus' route. 

>how many stops are on your route?: 

Again, only a positive integer is considered allowed input. However, this time the number
must be 2 or above. Like before, BusStop will keep asking until it receives valid input.

>Invalid input. There must be at least 2 stops on your route. Try again.

BusStop will take note of your number of stops, store it and move on.

At your first stop, BusStop will ask you how many passengers were waiting there.

>How many passengers were waiting for the bus at stop 1?: 

Only positive integers are accepted.   
Once BusStop has received valid input, it will store the number you wrote in, remind you
what you just wrote and give you a tally of the amount of passengers currently on the bus.

>You have entered:  15
>
>15 passengers on bus currently.

Once you have arrived at your next stop, BusStop will ask you how many passengers got off the
bus. Only positive integers are accepted, and the number input must be less than the total
amount of passengers on the bus currently. If a number larger than the total amount of
passengers on the bus is input, the following error will be shown, reminding you of the total
amount of passengers currently on the bus, and asking for input again.

>How many passengers got off at stop 2?: 16
> 
>you have entered:  16
> 
>Invalid input, there are only 15 passengers on the bus. Try again.

BusStop will keep asking for input until valid input is received.

Once it has taken note of your valid input, BusStop will continue this pattern of asking for
the amount of passengers that got off and then on the bus until you reach your final stop.

The busses of CodeTown have a maximum capacity of 47 passengers.   
If at any point there are more passengers than you have room for, input the whole amount
of customers hoping to board the bus. BusStop will take note that there were more passengers
than you could fit.

>How many passengers were waiting for the bus at stop 2?: 40
> 
>You have entered:  40
>
>No more customers can fit on the bus! 
>
>7  customers left behind!
>
>47 passengers on bus currently.

In this circumstance, as shown above, BusStop will let you know that there's no more room on
the bus, and tell you how many customers you need to leave behind.   
A tally of all customers left behind throughout your journey will be noted and saved for later.
Again, BusStop will remind you how many passengers you have on board.

Once your final stop, BusStop will let you know.    
It will automatically unload all the passengers from the bus in its system and then begin to 
print the results it had kept a note of from your journey.   
The information shown will be as follows:

>You have arrived at your final stop.
> 
>47 passengers left the bus.
> 
>Printing results...
> 
>Bus Route:  3
> 
>Amount of stops:  3
> 
>Happy customers:  48
> 
>Unhappy customers:  7
> 
>Ratio of happy to unhappy customers:  6.86

BusStop will repeat back the information that you told it including:  
- Route number
- Amount of stops on your journey
- Amount of "happy customers" (defined by customers
who were able to successfully board the bus and complete their journey)
- Amount of "unhappy customers" (defined by customers who were not able to board the bus
there was no room)
- Ratio of happy vs unhappy customers, given to the 2nd decimal place.

At this point BusStop will terminate. Feel free to write down this information, but
BusStop will record it in a text file and store it in the same directory where you've kept
BusStop.py.

Congratulations! You've successfully run BusStop, and are one step closer to making CodeTown
a better place!


### How it works:

#### Data:

All the important data stored by BusStop is in the dictionary 'information'.

```python
information = {  # holds all the information needed for the final result
    'Bus Route': 0,
    'Stop Amount': 0,
    'Happy Customers': 0,
    'Unhappy Customers': 0,
    'Ratio': '0.00'
}
```

There are also 2 global variables accessed by various functions within BusStop:

```python
# global variables to help certain functions keep track of passengers
on_bus = 0
left_behind = 0
```

#### Functions:

##### ask_route()   
Asks the driver for the route number.    
Accepts only positive integers. Stores the information in the dictionary 'information'
under key 'Route Number'.   


```python
def ask_route():
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
```

##### ask_stops()         
Asks the driver how many stops they have on their route.   
Accepts only positive integers from their input.
Stores the input in the dictionary 'information'
under key 'Stop Amount'.

```python
def ask_stops():
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
```

#### passenger_count()
Track passengers per stop.

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

This function is where the meat of the program is. As it is quite large snippets explaining
its working will be posted below.


```python
    for i in range(1, information.get('Stop Amount')):
        while True:
            try:
                psg_on = int(input("How many passengers were waiting for the bus at stop " + str(i) + "?: "))
                print('You have entered: ', psg_on)

                if psg_on < 0:
                    raise ValueError

                on_bus += psg_on

                print(on_bus, 'passengers on bus currently.')

                information['Happy Customers'] = int(information.get('Happy Customers')) + psg_on

                break
            except ValueError:
                print('Invalid input. You must use a positive integer. Please try again. ')
                continue
```

The above for loop is where the primary addition to the key 'Happy Customers' under 'information'
happens.   
Take input, assign it to 'psg_on,' converting it to an integer at the same time. Increment
key 'Happy Customers' by 'psg_on', as well as incrementing the global variable 'on_bus'.

Keep in mind that the for loop controls every part of the function, including the snippets 
below, it's length being dictated by the value of 'Stop Amount' which is a key of 'information'.


```python
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
```

The above if clause is the first statement nested within the for loop seen above.   
In fact, it actually appears before the above snippet, as the user needs to be asked if
there are passengers leaving the bus before adding new passengers for the calculations
to be correct.   
If the for loop is above 1, (Stop 2 has been reached) take input asking how many passengers
got off the bus. Assign it to 'psg_off'. There is an error raised if 'psg_off' is larger than
the global variable 'on_bus' as well as if 'psg_off' is a non integer type or negative.   
Decrease the global variable 'on_bus' by the value of 'psg_off'.


```python
if on_bus > 47:  # bus is full, increment 'Unhappy Passengers'
    print("No more customers can fit on the bus! ")
    for e in range(47, on_bus):
        on_bus -= 1
        left_behind = e - 47
        information['Unhappy Customers'] += 1
        information['Happy Customers'] -= 1  # Take from key as all passengers boarding increments key
        print(str(left_behind + 1), ' customers left behind!')
```

The above if clause is nested between the on_bus += psg_on and print(...) statements.  
If the bus reaches a patron count of above 47 (maximum capacity), tell the user they
have no more room on the bus. Then loop e many times between 47 and the value of the
global variable 'on_bus'. Decreasing 'on_bus' and 'Happy Customers' key of dictionary
'information' by 1 everytime. Everytime a passenger is recorded as coming on the bus,
the value of 'Happy Customers' is incremented by 1 which is why we must do this.   
The global variable 'left_behind' is given the value of e - 47, and we increment
the value of 'Unhappy Customers' key of dictionary 'information' by 1 as they weren't
able to board the bus. Then we remind the user how many customers they had to leave behind.

#### final_stop()

Facilitates the final stop on the bus' journey.   
Once the initial for loop in passenger_count() ends,
prints out how many passengers left the bus.
Doesn't need to modify any variables as that behaviour
is handled by passenger_count().   
Simple!

```python
def final_stop():
    global on_bus
    print('You have arrived at your final stop.')
    print(on_bus, 'passengers left the bus.')
```

#### print_results():

Print results to terminal and saves them for later viewing.   
Once the program has tallied up all the results, it prints
out everything in the dictionary 'information' to the
terminal, and then saves the contents of 'information' to
a text file for later viewing.

```python
def print_results():
    print('Printing results...')
    print("Bus Route: ", information['Bus Route'])
    print("Amount of stops: ", information['Stop Amount'])
    print("Happy customers: ", information['Happy Customers'])
    print("Unhappy customers: ", information['Unhappy Customers'])
    print("Ratio of happy to unhappy customers: ", information['Ratio'])
    f = open("Results.txt", "w")  # Create new .txt file
    f.write(str(information))
    f.close()
```

#### ratio(x,y):

Find the ratio of 2 numbers to 2 decimal points.

Key Arguments:   
x -- First term for division   
y -- Second term for division   

Coverts both key arguments to floats, and then
performs a division. It then stores the result
as a string, formatted to have 2 decimal places.
Stores the string in the dictionary 'information'
under key 'Ratio'.
If the result is 0, returns 0.00.   
In terms of the Dictionary 'information', the 'Ratio' key is already initialised at 0.00
so no changes need to be made.

```python
def ratio(x, y):
    try:
        val1 = float(x)
        val2 = float(y)
        result = val1 / val2
        result_str = f'{result:.{2}f}'  # Formats string to have 2 decimal places
    except ZeroDivisionError:
        return 0.00

    information['Ratio'] = result_str
```


The program itself runs with the following code:

```python
if __name__ == '__main__':
    ask_route()
    ask_stops()
    passenger_count()
    final_stop()
    ratio(information['Happy Customers'], information['Unhappy Customers'])
    print_results()
```


Thank you for reading.   
Alexander Robertson.