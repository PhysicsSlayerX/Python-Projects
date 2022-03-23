from itertools import count
from pynput import mouse

print("Program Running...")

browsers = 1
browser  = 1

#name_list = [
#    'Browser Icon (Taskbar)', 'Address Bar', '"Play Now!" Button', 
#    '"Connect Wallet" Button', 'Metamask Icon (Taskbar)', 'Metamask Confirmation', 
#    'Treasure Hunt', 'In-game Menu Arrow', 'Heroes Button', 'Character List (center)', 
#    'Work Button (All)', 'Rest Button (All)', 'Close Button (Char List)', 
#    'Back to Treasure Hunt', 'Back to Main Menu']

name_list1 = [];
for i in range(8):
    for j in range(3):
        name_list1.append(str(i+1)+str(j+1))

print(name_list1)

name_list2 = [];
for i in range(8):
    for j in range(4):
        name_list2.append(str(i+1)+str(j+4))

print(name_list2)

name_list = name_list1 + name_list2
print(name_list, len(name_list))

lines = []
count = 0

def on_click(x, y, button, pressed):
    global browsers
    global browser
    global count

    if button == mouse.Button.left and pressed:
        lines.append('{}'.format((x,y)))
        print('[Browser {}] {} at {}'.format(browser, name_list[count],(x,y)))
        count += 1
        if count == len(name_list):
            print("...Next Batch...")
    if count == len(name_list):
        browser += 1
        count = 0

    if browser > browsers:
        with open('realLoc3.txt', 'w') as f:
            f.write('\n'.join(lines))



listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()

