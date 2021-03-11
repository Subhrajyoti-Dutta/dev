from ctypes import CDLL

so_file = "C:\dev\Miscellaneous\mathematics.so"

my_math = CDLL(so_file)

my_math.printer(100000)