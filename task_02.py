#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""


import time


class Snapshot(object):
    """Current epoch time."""

    def __init__(self, created=time.time()):
        """Constractor for the Snapshot() class.

        Args:
            created(mixed): current Unix Timestamp.

        Attributes:
            created(mixed): current Unix Timestamp.
        """
        self.created = created
