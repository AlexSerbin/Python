class DigitalCounter:

    def __init__(self, minimum=0, maximum=100, current_val=0):
        self.minimum = minimum
        self.maximum = maximum
        self.current_val = current_val
        if current_val == 0:
            self.current_val = minimum
        if self.current_val > maximum:
            raise AssertionError('Current value  more then maximum value')
        if self.current_val < minimum:
            raise AssertionError('Current value  less then maximum value')

    def plus_one(self):
        self.current_val += 1
        if self.current_val > self.maximum:
            raise AssertionError('Can"'"t rise value more than maximum")

    def return_current_val(self):
        return self.current_val
