#ascii 8bit m1
def to2(k):
    re = ""
    while k > 1:
        re+= str(k%2)
        k = k//2
    re += str(k)
    return re[::-1]
    
    
print("This python program will help you convert your letter into ascii code in 8 bit")    
#print("enter your first 6 alphabet of your last-name : \n")
def main_p():
    last6 = str(input("enter your first 6 alphabet of your last-name :"))

    alpha = "abcdefghijklmnopqrstuvwxyz"
    b = 65
    string_dic = [] 

    for w in last6[:6:]:
        string_dic +=  [[w, to2(alpha.index(w)+b)]]
    print("your name in 2bit base : \n")
    for k in string_dic:
        print( k[0]," is ", k[1] , "\n" )
    return None

main_p()
    
