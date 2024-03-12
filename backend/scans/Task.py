from datetime import date 

from .DAL import dal
from scans.TaskManager import task_manager
from random import randint
import threading


class Task: 
    def __init__(self, task_id): 
        self.task_id = task_id
        self.switch = True

    def create(self, stream_ids):
        dal.models["tasks"].create({
            "task_id" : self.task_id, 
            "stream_ids" : stream_ids, 
            "status" : "PREPROCESSING", 
            "created_at" : str(date.today())
        }) 

    def update(self, status): 
        dal.models["tasks"].update(self.task_id, {
            "status" : status
        }) 

    def clear(self): 
        print(f"@ Clearing task ({self.task_id})...")

        self.switch = False

        print("@ Joining thread...")
        thread = task_manager.threads["tasks"][self.task_id] 
        thread.join() 
        
        del task_manager.threads["tasks"][self.task_id] 
        

    def runner(self, socket_io): 

        while True: 
        
            # Run task level operations.

                            
            socket_io.sleep(1) 

            if not self.switch:
                break

        pass