"""
Print tasks arrive once every 180 seconds. By arbitrarily choosing 180 from the range of random integers,
we can simulate this random event. The simulation function allows us to set the total time and
the pages per minute for the printer.
"""
from Queue.queue import Queue
from Queue.Printer.Printer import Printer
from Queue.Printer.Task import Task
import random


def simulation(num_seconds, pages_per_minute):  # Printer Simulation Function

    lab_printer = Printer(pages_per_minute)  # Create Printer Object referenced as 'lab_printer'
    print_queue = Queue()  # Create Queue Object referenced as 'print_queue'.
    waiting_times = []  # Create an Empty list as Waiting Time.

    for current_second in range(num_seconds):  # Run for loop on range 'num_seconds'

        if new_print_task():                # If function new_print_task() returns True then
            task = Task(current_second)     # create Task object referenced as 'task'
            print_queue.enqueue(task)       # append 'task' to print_queue from rear

        if (not lab_printer.busy()) and (not print_queue.is_empty()):  # If printer is not busy and print_queue is not empty
            next_task = print_queue.dequeue()  # Remove a task from front end of the Queue And assign it to a variable 'next_task'
            waiting_times.append(next_task.wait_time(current_second))  # Calculate waiting time of 'next_task' and append it to a list waiting_times
            lab_printer.start_next(next_task)  # Assign 'next task' to object 'lab_printer'

        lab_printer.tick()  # If current task is not None, decrement remaining time by 1.
                            # If remaining time is less than or equal to zero set current task to None

    average_wait = sum(waiting_times) / len(waiting_times)  # Calculate Average Waiting timing
    # Print Average Waiting timing and Queue Size
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def new_print_task():  # Function for Creating new print task
    num = random.randrange(1, 181)  # Select random number in between 1-180
    if num == 180:  # if number is 180 return True otherwise return False
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
