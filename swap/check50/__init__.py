from check50 import *

class Swap(Checks):

    @check()
    def exists(self):
        """swap.c exists"""
        self.require("swap.c")

    @check("exists")
    def compiles(self):
        """swap.c compiles"""
        self.spawn("clang -o swap swap.c").exit(0)

    @check("compiles")
    def swap_2_3(self):
        """swap switches two arbitray integers"""
        actual = "Swapped: X is 3 and Y is 2!\n"
        self.spawn("./swap").stdin("2\n3").stdout()
