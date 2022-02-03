def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1] + keys[0:-1]
    
    eDict= dict(zip(keys,value))
    dDict= dict(zip(value,keys))

    message= input("Please Input the message: ")
    mode= input("Mode (E or D): ")

    if mode.upper()== 'E':
        newMessage = ''.join([eDict[letter] for letter in message.lower()])
    
    elif mode.upper()== 'D':
        newMessage = ''.join([dDict[letter] for letter in message.lower()])

    else:
        print("Please enter correct choice")
    
    return newMessage

print(machine())