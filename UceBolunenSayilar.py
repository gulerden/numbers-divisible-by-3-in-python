print("1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.")

x=range(1,101)

for i in x:
    if(i%3==0):
        print(i)
    else:
        continue