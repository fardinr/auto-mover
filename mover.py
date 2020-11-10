import os
import time
from extensions import extension_paths


path = "E:\\User\\Fardin\\Demo projects\\auto mover\\test"
root_path = "E:\\User\\Fardin\\Demo projects\\auto mover\\test"
os.chdir(root_path)


def scan_file(path):
    path = "E:\\User\\Fardin\\Demo projects\\auto mover\\test"
    os.chdir(root_path)
    files = os.listdir(root_path)
    print("file", files)
    if not files:
        return
    for file in files:

        if os.path.isdir(file):
            continue
        else:

            # extension = file.split(sep=".")
            # print(extension)
            extension = os.path.splitext(file)[1][1:]
            extension = "."+extension
            print("extentions", extension)
            # print(extension_set)
            if extension_paths.get(extension):
                destination_path = extension_paths.get(extension)

            else:
                destination_path = extension_paths.get('noname')
            move(path, file, destination_path)
            # print(destination_path)
        return


def create_Folder(path, file, destination_path):

    try:
        os.makedirs(destination_path)
    except FileExistsError as e:
        print(e)
    path = path+"\\"+destination_path
    return


# Function to move files to respective folders


def move(path, file, destination_path):
    # destination_path.split("/")
    for split_path in destination_path.split("\\"):

        if os.path.exists("".join(split_path)):
            path = path+"\\"+split_path
            os.chdir(path)

            continue
        else:

            create_Folder(path, file, split_path)

            continue

    if os.path.exists(file):
        # print("'file exists'")
        increment = 0
        while True:
            increment += 1
            new_name = file[:0]+str(increment)+" "+file[0:]

            if not os.path.exists(new_name):
                os.chdir(path)
                try:
                    os.rename(root_path+"\\"+file, root_path+"\\" +
                              destination_path+"\\"+new_name)
                except (OSError, IndexError) as e:
                    print(e)

                break
        return

    else:
        os.chdir(path)
        try:
            os.rename(root_path+"\\"+file, root_path +
                      "\\"+destination_path+"\\"+file)
        except (OSError, IndexError) as e:
            print(e)
        return
    # print("move is called")
    # for file in files:
    #     fextension = os.path.splitext(file)[1][1:]

    #     # fextension = file.split(sep=".")
    #     try:
    #         os.rename(file, fextension+"_files/"+file)
    #     except (OSError, IndexError):
    #         continue


# Calling the functions in order
# create_Folder()
# move()
while(True):

    scan_file(path=path)
    # time.sleep(1)
