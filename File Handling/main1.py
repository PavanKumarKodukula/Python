import csv

# try:
#     with open("test.csv","w",newline="") as file:
#         writer = csv.writer(file)
#         header=["name","contact"]
#         writer.writerow(header)
#         data=[["ram",9876543210],["sam",8796543210]]
#         writer.writerows(data)
#         print("content added")
# except Exception as e:
#     print("something went wrong : {e}")  

try:
    with open("test.csv","r") as file:
        reader = csv.reader(file)
        contacts=list(reader)
        name=input()
        new_contact=input()
        for ind,row in enumerate(contacts):
            if row[0]==name:
                contacts[ind][1]=new_contact
                break
        else:
            print("contact name not exists")
except Exception as e:
    print(f"something went wrong : {e}")    

try:
    with open("test.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerows(contacts)
        print("content added")
except Exception as e:
    print(f"something wnet wrong in test.csv{e}")        
