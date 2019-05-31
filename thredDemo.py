#!/bin/python

import time, threading
print('starting the program...')

def TakeaNap():
    time.sleep(5)
    print('wake up!')

threadObj = threading.Thread(target=TakeaNap)
threadObj.start()

print('program terminated')

'''
Explanation why 'program terminated' appears before 'wake up'
If print('End of program.') is the last line of
the program, you might think that it should be the last thing printed. The
reason Wake up! comes after it is that when threadObj.start() is called, the tar-
get function for threadObj is run in a new thread of execution. Think of it as
a second finger appearing at the start of the takeANap() function. The main
thread continues to print('End of program.') . Meanwhile, the new thread
that has been executing the time.sleep(5) call, pauses for 5 seconds. After it
wakes from its 5-second nap, it prints 'Wake up!' and then returns from the
takeANap() function. Chronologically, 'Wake up!' is the last thing printed by
the program.
'''

