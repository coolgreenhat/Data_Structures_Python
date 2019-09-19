import random

class Task:
    def __init__(self,time):        # Create A task
        self.timestamp = time       # add current_second as time Stamp
        self.pages = random.randrange(1,21)  # Generate random number as number of pages

    def get_stamp(self):
        return self.timestamp       # return time_stamp of current task

    def get_pages(self):
        return self.pages           # return number of pages in current task

    def wait_time(self,current_time):
        return current_time - self.timestamp  # Subtract the timestamp from the current_second to compute the waiting time for that task.
