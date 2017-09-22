from check50 import *

class Square(Checks):

    @check()
    def exists(self):
        self.require("square.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o square square.c").exit(0)

    @check("compiles")
    def squares_0(self):
        self.spawn("./square 0").stdout("^0\n","0\n")
