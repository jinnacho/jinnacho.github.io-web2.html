n=""
while n!="y":
    a=int(input("월을 입력하세요"))
    if a>=3 and a<=5:
          print(a,"월은 봄입니다.")
          n=input("종료하시겠습니까?")
    elif a>=6 and a<=8:
          print(a,"월은 여름입니다.")
          n=input("종료하시겠습니까?")
    elif a>=9 and a<=11:
         print(a,"월은 가을입니다.")
         n=input("종료하시겠습니까?")
    else :
         print(a,"월은 겨울입니다.")
         n=input("종료하시겠습니까?")
           
print("종료되었습니다")      
