# Create Counter class
# which has an integer field value
# when creating it should have a default value 0 or we can specify it when creating
# we can add(number) to this counter another whole number
# or we can add() without parameters just increasing the counter's value by one
# and we can get() the current value
# also we can reset() the value to the initial value
# Check if everything is working fine with the proper test
# Download test_counter.py and place it next to your solution
# Run the test file as a usual python program

class Counter():

    def __init__(self, field = 0):
        self.default = field
        self.field = field

    def add(self, number = 1):
        self.field += number

    def get(self):
        print(self.field)
        return self.field

    def reset(self):
        self.field = self.default
