

def drawH():
    return ('H   H', 'H   H', 'HHHHH','H   H','H   H')

def drawY():
    return ('Y   Y',' Y Y ','  Y','  Y','  Y')

def drawI():
    return (' III ','  I  ','  I  ','  I  ',' III ')
def drawA():
    return('  A  ',' A A ','AAAAA','A   A','A   A')
    
def drawSpace():
    return ('  ')*5
    

#drawH()
#drawY()

while True:

    user_request = input("Please enter any text: ")
    funCollection = []

    for letter in user_request:
        
        if letter.upper() == "H":
            funCollection.append( drawH )
        elif letter.upper() == "Y":
            funCollection.append( drawY )
        elif letter.upper() == "I":
            funCollection.append( drawI )
        elif letter.upper() == "A":
            funCollection.append( drawA )
        elif letter.upper() == " ":
            funCollection.append( drawSpace )
        else:
            funCollection.append( drawSpace )
            

    for i in range(5):
        for f in funCollection:
            print (f()[i], end='\t')
        print()
