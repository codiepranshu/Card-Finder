from colorama import Fore,Style,Back
import random,itertools,emoji


main=[]
deck=list(itertools.product(range(1,14)))
print(emoji.emojize("    :spade_suit:")+Fore.RED+Style.BRIGHT+emoji.emojize("     :heart_suit:")+Style.RESET_ALL+emoji.emojize("      :club_suit:")+Fore.RED+Style.BRIGHT+emoji.emojize("       :diamond_suit:")+Style.RESET_ALL+Style.BRIGHT+Fore.CYAN+" GUESS"+Fore.RED+" ANY"+Fore.CYAN+" CARD     "+Style.RESET_ALL+emoji.emojize("    :spade_suit:")+Fore.RED+Style.BRIGHT+emoji.emojize("     :heart_suit:")+Style.RESET_ALL+emoji.emojize("      :club_suit:")+Style.RESET_ALL+Fore.RED+Style.BRIGHT+emoji.emojize("       :diamond_suit:"))
l=input()
print(Style.RESET_ALL)
#print(Back.YELLOW+"    sshhHHhSSss DONT TELL ssssSssHHH   ")
#print(Style.RESET_ALL)
#main=[2,5,83,16,86,23,44,17,15,38,29,10,63,286,19,22,33,44,55,66,77]
deck=list(itertools.product(range(1,10),["Spade","Heart","Diamond","Club"]))
random.shuffle(deck)
for i in range(21):
     print(deck[i][0],'of',deck[i][1])
for i in range(21):
     xy=deck[i][0],'of',deck[i][1]
     main.append(xy)
#print(main)
l=input()
print("\n")
print(emoji.emojize(":warning:")+Back.RED+"WARNING-> "+Style.RESET_ALL+emoji.emojize(":zipper-mouth_face:")+Style.BRIGHT+Fore.YELLOW+" DON'T TELL "+Style.RESET_ALL+emoji.emojize(":zipper-mouth_face:"))
print(Style.RESET_ALL)
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]
list10=[]
list11=[]
list12=[]
a=[]
main_list=[]
def shuffle_start():
    
    for val in range(0,21,3):
        
    
        list1.append(main[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.RED+"T"+Fore.RED+"ILE1")
    print(Style.RESET_ALL) 
    print(list1)
    l=input()
    for val in range(1,21,3):
    
        list2.append(main[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.RED+"TILE2")
    print(Style.RESET_ALL)    
    print(list2)
    l=input()
    for val in range(2,21,3):
    
        list3.append(main[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.RED+"TILE3")
    print(Style.RESET_ALL)    
    print(list3)
    l=input()
def shuffle(a):
    
    for val in range(0,21,3):
        
    
        list4.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.MAGENTA+"TILE1")
    print(Style.RESET_ALL)    
    print(list4)
    l=input()
    for val in range(1,21,3):
    
        list5.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.MAGENTA+"TILE2")
    print(Style.RESET_ALL)    
    print(list5)
    l=input()
    for val in range(2,21,3):
    
        list6.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.MAGENTA+"TILE3")
    print(Style.RESET_ALL)    
    print(list6)
    l=input()
    return 0
shuffle_start()

n=input(" **********ENTER THE NUMBER OF TILE**************      ")
if n=="1":
    main_list=list2+list1+list3
    b=shuffle(main_list)
    #print(main_list)
    
elif(n=="2"):
    main_list=list1+list2+list3
    b=shuffle(main_list)
    #print(b)
    
elif(n=="3"):
    main_list=list1+list3+list2
    b=shuffle(main_list)
    #print(b)
else:
    print("invalid output")
q=input("************ENTER THE NUMBER OF TILE**************      ")
def shuff(a):
    
    for val in range(0,21,3):
        
    
        list7.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.RED+"TILE1")
    print(Style.RESET_ALL)    
    print(list7)
    l=input()
    for val in range(1,21,3):
    
        list8.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.RED+"TILE2")
    print(Style.RESET_ALL)    
    print(list8)
    l=input()
    for val in range(2,21,3):
    
        list9.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.RED+"TILE3")
    print(Style.RESET_ALL)    
    print(list9)
    l=input()
    return 0
if q=="1":
    main_list=list5+list4+list6
    b=shuff(main_list)
    #print(main_list)
    
elif(q=="2"):
    main_list=list4+list5+list6
    b=shuff(main_list)
    #print(b)
    
elif(q=="3"):
    main_list=list4+list6+list5
    b=shuff(main_list)
    #print(b)
else:
    print("invalid output")
def shuf(a):
    
    for val in range(0,21,3):
        
    
        list10.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.MAGENTA+"TILE1")
    print(Style.RESET_ALL)    
    print(list10)
    l=input()
    for val in range(1,21,3):
    
        list11.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.MAGENTA+"TILE2")
    print(Style.RESET_ALL)    
    print(list11)
    l=input()
    for val in range(2,21,3):
    
        list12.append(a[val])
    print(Fore.CYAN+emoji.emojize(":collision:")+Style.BRIGHT+Fore.MAGENTA+"TILE3")
    print(Style.RESET_ALL)    
    print(list12)
    l=input()
    
    return 0
f=input("************ENTER THE NUMBER OF TILE****************      ")    
if f=="1":
    main_list=list8+list7+list9
    b=shuf(main_list)
    #print(main_list)
    
elif(f=="2"):
    main_list=list7+list8+list9
    b=shuf(main_list)
    #print(b)
    
elif(f=="3"):
    main_list=list7+list9+list8
    b=shuf(main_list)
    #print(b)
else:
    print("invalid output")
g=input("**************ENTER THE NUMBER OF TILE****************       ")    
if g=="1":
    main_list=list11+list10+list12
    #b=shuf(main_list)
    #print(main_list)
    
elif(g=="2"):
    main_list=list10+list11+list12
    #b=shuf(main_list)
    #print(main_list)
    
elif(g=="3"):
    main_list=list10+list12+list11
    #b=shuf(main_list)
    #print(main_list)
else:
    print("invalid input")
print("     YOUR NUMBER IS    ",main_list[10])    
        
        

    
    
    
    
    