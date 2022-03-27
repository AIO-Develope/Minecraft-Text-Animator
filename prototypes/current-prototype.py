u_text = input("Text: ")
format = input("format: ")
color = input("color: ")

def split(u_text):
    return [char for char in u_text]
     
c_text = len(u_text)
s_text = split(u_text)



f = open('output.txt', 'r+')
f.truncate(0)

if format == "Raw":

    for i in range(c_text + 1):
        s_text.insert(i, color)
        s_text.insert(i + 2, '&r')
        print("".join(s_text))
        
        f = open("output.txt", "a")
        f.write("".join(s_text) + "\n")
        f.close()

        try:
            
            del s_text[i + 2]
            del s_text[i]
        except:
            pass

elif format == "Tab":
    for i in range(c_text + 1):
        s_text.insert(i, color)
        s_text.insert(i + 2, '&r')
        print("  - '" + "".join(s_text) + "'")
        
        f = open("output.txt", "a")
        f.write("  - '" + "".join(s_text) + "'\n")
        f.close()
    
        
        try:
            
            del s_text[i + 2]
            del s_text[i]
        except:
            pass

elif format == "Scoreboard":
    for i in range(c_text + 1):
        s_text.insert(i, color)
        s_text.insert(i + 2, '&r')
        print("        - '" + "".join(s_text) + "'")
        
        f = open("output.txt", "a")
        f.write("        - '" + "".join(s_text) + "'\n")
        f.close()
    
        
        try:
            
            del s_text[i + 2]
            del s_text[i]
        except:
            pass



