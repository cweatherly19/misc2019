x = 0
y = 0
z = 0
xo = x; yo = y; zo = z

def read():
    f = open("xyz.txt", "r")
    f.seek(0)
    n = 1 + int(f.readline())
    f.seek(n)
    x = int(f.readline())
    f.seek(2 * n)
    y = int(f.readline())
    f.seek(3 * n)
    z = int(f.readline())
    f.close()
    return x, y, z
#or, readlines reads the individual line into a list



if __name__== "__main__":
    x, y, z = read()
    print x; print y; print z


# find how to only update if there's a change, not continuously
