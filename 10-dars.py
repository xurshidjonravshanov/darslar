# KARA KARA
# sonlar2 = list(range(11))
# sonlar = list(range(11))
# for n in sonlar2:
#     for i in sonlar:
#         print(f" {n} x {i} = {n*i}")
        
        
# sonlar2 = list(range(1, 11))
# sonlar = list(range(1 , 11))
# for n in sonlar2:
#     for i in sonlar:
#         print(f" {n} x {i} = {n*i}")
# savol = int(input("Yoshingiz nechida?>>> "))
# if savol <= 4 :
#     print("Sizga kirish bepul")
# elif savol <=12:
#     print("Sizga kirish 5000 so`m ")
# elif savol <= 18:
#     print("Sizga kirish 8000 so`m ")
# else:
#     print("Sizga kirish 10000 so`m")                
# son = int(input("Istalgan son kiriting>>> "))
# for n in range(10):
#     print(f"{n} + {son} = {n+son}")


# kun = input("Bugun nima kun?>>> ")
# if kun.lower() =='shanba' or kun.lower() =='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni ")
# kun = input("Bugun nima kun?>>> ")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower() == 'yakshanba' or kun.lower()== 'shanba' and harorat>=30:
#     print("Cho`milgani ketdik !")
# elif kun.lower()== 'yakshanba' or kun.lower()=='shanba' and harorat<=30:
#     print("Uyda dam olamiz")
# choy = False
# coffee = True
# salat = True
# price = 15000
# if choy and salat:
#     price = price + 10000
# elif choy or salat:
#     print(f"Jami {price} so`m")    
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 6000
# if salat:
#     print("Mijoz salat oldi .")
#     narh = narh + 8000
# if non:
#     print("Mijoz non oldi. ")
#     narh = narh + 9000
# if kompot:
#     print("Mijoz kompot oldi")
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000

# print(f"Jami {narh} so`m ")    
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz?>>> ")
# if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo`q ")
# else:
#     print("Buyurtma qabul qilindi ")    
# yil = "2020"
# print(yil.isdigit())  
# yil1 = "Ikki"
# print(yil1.isalnum())    
menu = ['osh', 'qozokabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

if buyurtmalar:
    for taom in buyurtmalar:
        for taom in menu:
            print(f"Menuda {taom} yo`q")
        else:
            print(f"Kechirasiz, menuda {taom} yo`q")
else:
    print("Savatchangiz bo`sh")            
    

    
    
    
    
    
    
    
    
    
    
    