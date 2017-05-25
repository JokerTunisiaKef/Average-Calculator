# Calculating Average

print "Average Calculator with python by Ahmed Ayari"

AVR = 0.0
global NUM
NUM = 0

Subjects = ["Math","Svt","Physiq","His","Geo","Islmq","Civiq","Arb","Fr","Eng",
            "Tech","Info","Sprt"]

def avr(b,c) :
    global NUM
    Sum = 0.0
    NUM += c
    a = [float(raw_input("    "+str(i+1)+"_")) for i in range(b)]
    for i in range(b) :
        Sum += a[i]
    Sum += a[b-1]
    return (Sum/(b+1))*c

for i in range(13) :
    print Subjects[i]+" : "
    AVR += avr(int(raw_input("   Tests' Number : ")),int(raw_input("   Subject 's Coefficient : ")))
    print " "
    
print "Your average is : " +str(AVR/NUM) + " - (hhfhfhhhhhhhfh ;) )"

for i in range(10000000) :
    AVR = 3
    
    

    


            
