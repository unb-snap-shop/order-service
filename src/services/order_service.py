from ..interfaces.observer_interface import Observer

class OrderService:
    def __init__(self):
        self.observers = []
        self.cart = {}

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def add_to_cart(self, user_id: str, product_id: str, quantity: int):
        self.notify_observers(f"Product {product_id} added to cart for user {user_id}")