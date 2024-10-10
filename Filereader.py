from dataclasses import dataclass

from loguru import logger


@dataclass
class Reading:

    """Small container class representing a single voltage readingg
    """

    timestamp: float
    adc:int

    def voltage(self):
        """Convert ADC reading to a physical voltage [V]
        """
        return 1.653 * self.adc + 0.456

#    def __str__(self):
#        return f'Reading at {self.timestamp} s: {self.adc} ADC counts ({self.voltage()} V)'



class VoltageData:

    """Simple interace to a set of voltage readings
    """

    def __init__(self, file_path):
        with open(file_path) as input_file:
            self._readings = [self._parse_line(line) for line in input_file.readlines()]
        logger.info(f'Done, {len(self._readings)} values read')
        self._iterator = iter(self._readings)


    @staticmethod
    def _parse_line(line):
        """Parse a single line from a text file and return a Reading object
        """
        timestamp, adc = line.split()
        timestamp = float(timestamp)
        adc = int(adc)
        return Reading(timestamp, adc)


    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iterator)

    def __getitem__(self, index):
        return self._readings[index]


if __name__ == '__main__':
    data = VoltageData('voltage_data.txt')
    for reading in data:
        print(reading)

    print ('Done')
    print(data[3])