# file = open("sample.txt","w")
# file.write("Good Morning Everyone")
# file.close()
# print("Content Added")

# file = open("sample.txt","a")
# file.write("I am Pavan Kumar")
# file.close()
# print("Content Added")

# file = None
# try:
#     file = open("sample.txt","r")
#     data=file.read()
#     print(data)
# except Exception as e:
#     print(f"something wrong because: {e}")
# finally:
#     if file is not None:
#         file.close()

file = None
try:
    file = open("sample.txt","r")
    data=file.readlines()
    print(data)
except Exception as e:
    print(f"something wrong because: {e}")
finally:
    if file is not None:
        file.close()
