import zipfile

def main():

    for i in range(500, -1, -1):
        filename = 'kletva_'+str(i)+'.zip'
        print(filename)
        f = open("stranica.txt", "r")
        output = f.readline()
        pswd = str(int(eval(output)))
        print(pswd)
        with zipfile.ZipFile(filename, 'r') as file:
            file.extractall(pwd = bytes(pswd, 'utf-8'))

    f2=open("flag.txt", "r")
    print(f2.readline())
    return 0

if __name__ == "__main__":
    main()