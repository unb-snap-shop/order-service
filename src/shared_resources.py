from queue import Queue

# Creating a queue for the observer pattern. 
# This is required so that the same queue can be passed from ui_observer.py to routes.py
messages_queue = Queue()
