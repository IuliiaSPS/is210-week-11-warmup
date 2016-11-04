#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


import produce


TOMATO = produce.Produce()

TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT = produce.Produce(1311210802)

EGGPLANT_EXPIRES = produce.Produce.get_expiration(EGGPLANT)
