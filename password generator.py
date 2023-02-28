import random
while True:
    z=input("Do you want to generate password? :")
    y="yes"
    x="no"
    b=["1","2","3","4","5","6","7","8","9"]
    c=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    p=["!","@","#","$","%","&"]
    d=random.choice(b)
    e=random.choice(c)
    f=random.choice(p)
    g=random.choice(b)
    h=random.choice(c)
    i=random.choice(a)
    j=random.choice(p)
    k=random.choice(c)
    l=random.choice(a)
    m=random.choice(b)
    n=random.choice(c)
    o=random.choice(p)
    if z==y:
        print(f"{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}")
    else:
        print("Bye-bye")
        break
