class MobileNumerologyCalculator:

    def __init__(self, mobile_number):
        self.mobile_number = str(mobile_number)

    def get_digits(self):
        return [int(d) for d in self.mobile_number]

    def calculate_compound_number(self):
        digits = self.get_digits()
        return sum(digits)

    def calculate_root_number(self):
        compound = self.calculate_compound_number()

        while compound > 9:
            compound = sum(int(d) for d in str(compound))

        return compound

    def digit_frequency(self):
        frequency = {i: 0 for i in range(10)}

        for digit in self.mobile_number:
            frequency[int(digit)] += 1

        return frequency

    def analyze(self):
        compound = self.calculate_compound_number()
        root = self.calculate_root_number()
        freq = self.digit_frequency()

        return {
            "mobile_number": self.mobile_number,
            "compound_number": compound,
            "root_number": root,
            "digit_frequency": freq
        }
