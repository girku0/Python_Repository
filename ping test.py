
import os

fp = open(r"C:\\Users\\Thibault\\PycharmProjects\\test\\hostname.csv", 'w')
with open("C:\\Users\\Thibault\\PycharmProjects\\test\\hostname.csv", 'a') as fp:
    for i in range (0,255):
        for j in range(1,254):
            hostname = "10.222.{0}.{1}".format(i,j)
            response = os.system ("ping -n 1 " + hostname)
            if response == 0:
                fp.writelines(hostname + "host up\n")
            else:
                fp.write(hostname + "host dead\n")