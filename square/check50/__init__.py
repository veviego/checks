from check50 import *

class Square(Checks):

    @check()
    def exists(self):
        """square.c exists"""
        self.require("square.c")

    @check("exists")
    def compiles(self):
        """square.c compiles"""
        self.spawn("clang -o square square.c").exit(0)

    @check("compiles")
    def squares_0(self):
        """square.c computes square of 0 as 0"""
        self.spawn("./square 0").stdout("^0\n","0\n")

    @check("compiles")
    def squares_28(self):
        """square.c computes square of 28 as 784"""
        self.spawn("./square 28").stdout("^784\n","784\n")
