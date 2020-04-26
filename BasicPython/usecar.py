from Car import *

# สร้าง Object หรือ Instance ของ Class Car
objcar1 = Car('red', 'Toyota', 4, 4, 180)
objcar1.printdata()

print('')

objcar2 = Car('', '', '', '', '')
objcar2.setbrand("Honda")
objcar2.setcolor("White")
objcar2.setspeed(150)

objcar2.printdata()
