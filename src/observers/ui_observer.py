from ..interfaces.observer_interface import Observer
from src.shared_resources import messages_queue


# using the queue class since it is thread safe!
class UIObserver(Observer):
    def update(self, message: str):
        print("UI Observer receiving: " + message)
        messages_queue.put(message)  # appending message to global queue to update the UI
