class Jar:
    def __init__(self, capacity=12, cookies=0):
        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return f"You have {self.cookies} cookies. Max of {self.capacity} cookies"

    def deposit(self, add_cookies):
        if add_cookies < 0:
            raise ValueError("No negative")
        self.cookies = self.cookies + add_cookies

    def withdraw(self, take_cookies):
        if take_cookies < 0:
            raise ValueError("No negative")
        if take_cookies > self.cookies:
            raise ValueError("You don't have that amount of cookies")
        self.cookies = self.cookies - take_cookies

    # Getter for jar capacity
    @property
    def capacity(self):
        return self._capacity

    # setter for jar capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    # Getter for n of cookies in jar
    @property
    def cookies(self):
        return self._cookies

    # Setter for n of cookies in jar
    @cookies.setter
    def cookies(self, cookie):
        if cookie < 0:
            raise ValueError("No negative cookies allowed")
        if cookie > self.capacity:
            raise ValueError("Too many cookies")
        self._cookies = cookie
