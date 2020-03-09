import sys

infile = open(sys.argv[3],"r")
plaintext = infile.read()
outfile = open(sys.argv[4],"w")

if sys.argv[1] == "shift" :
    if sys.argv[2] == "encrypt" :
        a = int(sys.argv[5])
        for i in plaintext :
            x = i
            if x != " " and x != "\n" :
                x = (ord(x) - ord('A') + a) % 26
                x = chr(x + ord('A'))
            outfile.write(x)
    else :
        a = (-int(sys.argv[5]) + 26) % 26
        for i in plaintext :
            x = i
            if x != " " and x != "\n" :
                x = (ord(x) - ord('A') + a) % 26
                x = chr(x + ord('A'))
            outfile.write(x)


elif sys.argv[1] == "affine" :
    if sys.argv[2] == "encrypt" :
        a = int(sys.argv[5])
        b = int(sys.argv[6])
        for i in plaintext :
            x = i
            if x != " " and x != "\n" :
                x = ord(x) - ord('A')
                x = (x * a + b) % 26 
                x = chr(x + ord('A'))
            outfile.write(x)
    else :
        a = int(sys.argv[5])
        for i in range(26) :
            if ((a * i) % 26) == 1 :
                a = i
            
        b = (-int(sys.argv[6]) + 26) % 26
        for i in plaintext :
            x = i
            if x != " " and x != "\n" :
                x = ord(x) - ord('A')
                x = ((x + b) * a) % 26 
                x = chr(x + ord('A'))
            outfile.write(x)


elif sys.argv[1] == "vigenere" :
    temp = sys.argv[5]
    sz = len(temp)
    cnt = 0
    key = []
    for i in plaintext :
        if i != " " and i != "\n" :
            key.append(temp[cnt])
            cnt = (cnt + 1) % sz
        else :
            key.append(i)

    if sys.argv[2] == "encrypt" :
        for i in range(len(plaintext)) :
            if key[i] != " " and key[i] != "\n" :
                x = ord(plaintext[i]) - ord('A')
                y = ord(key[i]) - ord('A')
                z = (x + y) % 26
                z = chr( z + ord('A')) 
                outfile.write(z)
            else :
                outfile.write(key[i])
                
        
    else :
        for i in range(len(plaintext)) :
            if key[i] != " " and key[i] != "\n" :
                x = ord(plaintext[i]) - ord('A')
                y = ord(key[i]) - ord('A')
                z = (x - y + 26) % 26
                z = chr( z + ord('A')) 
                outfile.write(z)
            else :
                outfile.write(key[i])        


    
            
        
    
        
            
            
        
        