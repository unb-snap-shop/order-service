from ..interfaces.observer_interface import Observer

class UIObserver(Observer):
    def update(self, message: str):
        # Code to update the UI based on the message
        print(f"UI updated with message: {message}")
