import pyperclip
def p():
    while True:
        
        text = pyperclip.paste()
        print(text)
        result = " ".join(text.split())
        result =result.replace("."," ")
        pyperclip.copy(result)
        print(result)
        input('Press any key to continue or Ctrl+C in console to exit')
p()
