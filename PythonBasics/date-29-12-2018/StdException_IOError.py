#f=open("file1.txt",'r')
#
#f.write("Welcome")

#Above code throws IO.Unsupported Error file is opened for reading and write operation not permitted

try:
    f=open("file1.txt",'r')
    f.write("Welcome")
except Exception as e:
    print(type(e))