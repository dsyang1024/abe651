"""
This is function drawing grid.
"""

def print_grids():
    # this function will draw entire grids
    print_grid()
    print_grid()
    print_grid()
    print_grid()
    maketopbtm(bytesize)

def print_grid():
    # this function will draw single row of the grids
    # each box will be 4 byte size
    '''
    +----+
    l    l
    l    l
    l    l
    l    l
    +----+
    '''
    maketopbtm(bytesize)
    makemid(bytesize)
    makemid(bytesize)
    makemid(bytesize)
    makemid(bytesize)


# the box will be divided into two parts (top/bottom and middle)
# below function is drawing top and bottom part of the grid
def maketopbtm(bytesize):
    # bytesize will determine horizontal distance of the grid
    print('+',end='')
    print('-'*bytesize,end='')
    print('+',end='')
    print('-'*bytesize,end='')
    print('+',end='')
    print('-'*bytesize,end='')
    print('+',end='')
    print('-'*bytesize,end='')
    print('+')


# below function is drawing mid part of the grid
def makemid(bytesize):
    # bytesize will determine horizontal distance of the grid
    print('|',end='')
    print(' '*bytesize,end='')
    print('|',end='')
    print(' '*bytesize,end='')
    print('|',end='')
    print(' '*bytesize,end='')
    print('|',end='')
    print(' '*bytesize,end='')
    print('|')



# the following condition checks whether we are running as a
# script (like when you test the code), in which case run the
# test code, or being imported (say by the autograder), in
# which case don't.  Your main code should be "indented"
# within this conditional, just like the example code.

if __name__ == '__main__':
    bytesize = 4
    # make this statement produce a 4x4 grid on the screen
    print_grids()
