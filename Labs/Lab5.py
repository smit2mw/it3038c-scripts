def countCharacter(str): 
    
    vowels = 0
    consonant = 0
    totalLetters = 0 

    for i in range(0, len(str)):  
          
        ch = str[i]  
  
        if ( (ch >= 'a' and ch <= 'z') or 
             (ch >= 'A' and ch <= 'Z') ):  
  
            # To change upper case to lower case for shorter code 
            ch = ch.lower() 
  
            if (ch == 'a' or ch == 'e' or ch == 'i' 
                        or ch == 'o' or ch == 'u'): 
                vowels += 1
                totalLetters +=1
            else: 
                consonant += 1
                totalLetters +=1
          

    print("Vowels:", vowels) 
    print("Consonant:", consonant)  
    print("Total Letters:", totalLetters)
  
str = input("Enter you word or phrase: ")
countCharacter(str)
