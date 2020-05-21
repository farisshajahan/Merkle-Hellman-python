import random 
import string 
  
def randStrGenerator(size): 
      
    # Takes random choices from ascii_letters and digits 
    generate_str= ''.join([random.choice( 
                        string.ascii_letters + string.digits) 
                        for n in range(size)]) 
                          
    return generate_str 
  
# Driver Code 
f = open("RandomStrings.txt", "w")
for i in range(20000):
    rand_string = randStrGenerator(149) 
    f.write(rand_string)
    f.write("\n")

f.close()
