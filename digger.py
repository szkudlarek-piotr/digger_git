import os
start = r"C:\Users\Piotr Szkudlarek"
folders_list = [start]
all_folders = []
while True:
    new=[]
    for i in folders_list:
        try:
            for j in os.listdir(i):
                con = os.path.join(i,j)
                if os.path.isdir(con):
                    new.append(con)
                    all_folders.append(con)
        except:
            print("Odmowa dostępu w {}.".format(i))
    folders_list = new
    if len(new) == 0:
        break
excele = []
print(all_folders)
for i in all_folders:
    for j in os.listdir(i):
        if ".xlsx" in j:
            excele.append(os.path.join(i,j))
wakacje = []
for i in excele:
    print(i)