####################################################################
#   Aaren Patel
#   I pledge my honor that I have abided by the Stevens Honor System
#   12/7/22
#   Cs 115 - HW 12
####################################################################
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new Date object with the same values as the input Date object"""
        return Date(self.month, self.day, self.year)

    def equals(self, d2):
        """Returns True if the two Date objects share the same calandar day, else with return False"""
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        """Changes the day to after the input Date object"""
        self.day += 1
        if self.day > DAYS_IN_MONTH[self.month]:
            if self.month != 2 or (self.month == 2 and not self.isLeapYear()):
                self.day = 1
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
            elif self.day > 29:
                self.month = 3
                self.day = 1


    def yesterday(self):
        """Changes the day to before the input Date object"""
        self.day -= 1
        if self.day == 0:
            self.month -= 1
            if self.month == 0:
                self.year -= 1
                self.month = 12
            self.day = DAYS_IN_MONTH[self.month]
            if self.month == 2 and self.isLeapYear():
                self.day += 1

    def addNDays(self, N):
        """Adds n amount of days to the input Date"""
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        """Goes back n amount of days to the input Date"""
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        """Returns True if self is before d2, else returns False"""
        if self.year < d2.year or (self.year == d2.year and ((self.month == d2.month and self.day < d2.day) or self.month < d2.month)):
            return True
        return False

    def isAfter(self, d2):
        """Returns True if self is after d2, else returns False"""
        if self.year > d2.year or (self.year == d2.year and ((self.month == d2.month and self.day > d2.day) or self.month > d2.month)):
            return True
        return False

    def diff(self, d2):
        """Returns the number of days of self - d2"""
        count = 0
        d1 = self.copy()
        while d1.isBefore(d2):
            count -= 1
            d1.tomorrow()
        while d1.isAfter(d2):
            count += 1
            d1.yesterday()
        return count

    def dow(self):
        dow = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        d = Date(12, 3, 2022)
        return dow[self.diff(d) % 7]

