

def drawH():
    print('''
H   H
H   H
HHHHH
H   H
H   H
 
''')

def drawY():
    print('''
Y   Y
 Y Y 
  Y
  Y
  Y
''')


def drawI():
    print('''
 III 
  I  
  I  
  I  
 III 
''')

def drawA():
    print('''
   A  
  A A 
 AAAAA
 A   A
 A   A
 ''')
    
def drawSpace():
	print('''
	
	
	
	
	''')

    

#drawH()
#drawY()

user_request = input("Please enter any text: ")

for letter in user_request:
    #print(letter)
    if letter.upper() == "H":
        drawH()
    elif letter.upper() == "Y":
        drawY()
    elif letter.upper() == "I":
        drawI()
    elif letter.upper() == "A":
        drawA()
    elif letter.upper() == "Y":
        drawSpace()
