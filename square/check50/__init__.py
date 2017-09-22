from check50 import *

class Square(Checks):

    @check()
    def exists():
        self.require("square.c")

    @check("exists")
    def compiles():
        self.spawn("clang -o square square.c").exit(0)

    @check("compiles")
    def squares_0():
        self.spawn("./square 0").stdout("^0\n","0\n")
