import keyboard  # using module keyboard

print("waiting for input...")

while True:  # making a loop
    #try: 
       # if keyboard.is_pressed('q'):  # if key 'q' is pressed 
           # print('You Pressed A Key!')
           # break  # finishing the loop
   # except:
    #    print('you presssed another key!')
     #   break  # if user pressed a key other than the given key the loop will break
    if keyboard.is_pressed('q'):
        print('you pressed q!')

    elif keyboard.is_pressed('x'):
        print('exiting...')
        break

