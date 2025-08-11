try:
    with open("text01.txt" , "r")as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("text02.txt" , "r")as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("text0.txt" , "r")as f:
        print(f.read())
except Exception as e:
    print(e)

print("thankyou")