import os


def get_cpp():
    global pathh
    global file1
    global file2

    #pathh = str(input("path: "))
    f = open("dataa.txt", "r")
    pathh = f.readlines()[0]
    pathh = pathh.rstrip('\n')
    #pathh.replace("\n", "")
    #print(pathh)
    f.close()

    ii = 0
    for i in pathh:
        if i == "/" or i == "\\":
            file1 = pathh.replace(pathh[:ii], '')
            file1 = file1.replace(i, '')
            #print(file1)
        ii += 1


get_cpp()


file1 = str(file1)
file2 = str(file1.replace('.cpp', ''))

pathh = pathh.replace(file1, '')


def main():
    runn = False
    while not runn:
        #print("\n\npathh: " + pathh + "\n\n")
        #print("\n\nfile1: " + file1 + "\n\n")
        #print("\n\nfile2: " + file2 + "\n\n")

        # If your cpp file is in other drive (for example E), then rename D: with E:
        # in the line of code below.
        #print(f'{pathh}\n{file2}{file1}')
        os.system(f'cmd /k "D: && cd {pathh} && g++ -o {file2} {file1} && {file2}.exe"')
        runn = True


main()
