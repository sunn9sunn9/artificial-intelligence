x = input("Введите ваше число: ")
xf = float(x)
if xf<-5:
    print("Ваше число принадлежит интервалу (-infinity, -5)")
elif xf<5:
    print("Ваше число принадлежит интервалу (-5, 5)")
else:
    print("Ваше число принадлежит интервалу (5, +infinity)")