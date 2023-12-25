try:

    def btd(num):
        l = list(str(num))
        l = list(str(num))
        l.reverse()
        m = 0
        ll = len(l) - 1
        print(l)
        while ll>=0:
            m +=int(l[ll])*(2**ll)
            print(ll)
            ll -=1
        print(f'your converted dachimal :{m}')
        
    
    btd(int(input("Enter Binary number:")))
except:
    print("Please Enter orrect Value ......😟😟")

    


    
