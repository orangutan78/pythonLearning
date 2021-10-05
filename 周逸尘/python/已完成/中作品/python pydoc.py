from pykeyboard import PyKeyboard
from time import sleep
kbd=PyKeyboard()
kbd.press_key(kbd.windows_l_key)
kbd.tap_key('r')
kbd.release_key(kbd.windows_l_key)
sleep(0.2)
kbd.tap_key('c')
kbd.tap_key('m')
kbd.tap_key('d')
kbd.tap_key(kbd.enter_key)
sleep(0.5)
kbd.tap_key('c')
kbd.tap_key('o')
kbd.tap_key('l')
kbd.tap_key('o')
kbd.tap_key('r')
kbd.tap_key(kbd.space_key)
kbd.tap_key('6')
kbd.tap_key('1')
kbd.tap_key(kbd.enter_key)
sleep(0.2)
strings='python -m pydoc -b\r'
turn=0
for i in range(len(strings)):
    kbd.tap_key(strings[turn])
    turn+=1
