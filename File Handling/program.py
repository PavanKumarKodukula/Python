file=None
try:
    file=open("output.txt","w")
    num=10
    for i in range(1,num+1):
        file.write(str(i)+"\n")
except:
    print("something wrong")
finally:
    if file is not None:
        file.close()            