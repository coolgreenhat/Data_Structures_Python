# Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
class Printer:
    def __init__(self,ppm): # Create a Printer Object With given page_rate, current task as None, remaining time as 0
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:        # If current task is not None , decrement remaining time by 1.
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:    # If remaining time is less than or equal to zero set current task to None.
                self.current_task = None

    def busy(self):
        if self.current_task != None:   # If Current task is not None return As Busy(True),Otherwise Return as Not Busy.
            return True
        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task    # To start next task Set Current task as New Task(Object)
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate # time required is Calculated by number of pages
                                                                        # multiplied by seconds(60) divided by page rate