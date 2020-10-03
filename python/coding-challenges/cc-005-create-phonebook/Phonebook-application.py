#  Create Phonebook Application

while True:
    num = input('''Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) : ''') 
    dic = {}
    for i in range (5):
        
        # Find phone number
        if i == 1: 
            pass
        
        #Insert a phone number
        elif i == 2:
           name= input("Insert name of the person : ") 
           phone_num = input("Insert phone number of the person")
           if not name.isnumeric() and not phone_num.isdecimal():
               print("Invalid input format, cancelling operation ...")
           else:
               dic.append(name, phone_num)
              
        #Delete a person from the phonebook
        elif i == 3:
            pass
        
        #Terminate
        elif i == 4:
            print("Existing the phonebook... Good Bye")
            
        else:
            print("Bir kez daha deneyiniz.")
    break
    
