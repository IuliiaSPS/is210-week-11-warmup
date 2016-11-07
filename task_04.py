#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_04"""


import car


class CustomCar(car.Car):
    """Modified Car() class"""

    def __init__(self, color='red', tires=None):
        """Constructor for the CustomCar() class.

        Args:
            color (string): The color of the car. Defaults to 'red'.
            tires (list): a list of CustomTire() objects.

        Attributes:
           color (string): The color of the car.
           tires (list): a list of CustomTire() objects.
        """
        if tires is None:
            tires = []
            for _ in range(4):
                tires.append(CustomTire())
        car.Car.__init__(self, color)
        self.tires = tires


class CustomTire(car.Tire):
    """Tire for customer."""

    def __init__(self):
        """Constructor for the CustomTire() class."""
        self.__maximum_miles = 500
        car.Tire.__init__(self, miles=0)
