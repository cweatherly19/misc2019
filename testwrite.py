# the \n is what makes a new line
n = 1
x = 3
y = 9
z = 2


def main():
    f = open("xyz.txt","w+")
    L = [("%d\n" % n), ("%d\n" % x), ("%d\n" % y), ("%d\n" % z)]
    f.writelines(L)
    f.close()


if __name__== "__main__":
    main()


# File_object.writelines(L) for L = [str1, str2, str3]
