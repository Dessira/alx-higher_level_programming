#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, value):
        """Overide equals"""

        return super().__ne__(value)

    def __ne__(self, value):
        """Overide not equals"""

        return super().__eq__(value)
