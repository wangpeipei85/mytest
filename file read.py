import time
import threading


def write1(i):
    with open(r"write test.dat", "w") as f:
        for ll in range(i):
            f.write('line %s\n' % ll)
            print('writen line %s' % ll)
            f.flush()
            time.sleep(1)


def read1():
    with open(r"write test.dat", "r") as f1:
        aa = f1.readline()
        while aa:
            print('read', aa)
            aa = f1.readline()
        # time.sleep(0.1)

if __name__ == '__main__':
    # thread1 = threading.Thread(target=(lambda: write1(11111)))
    # thread1.start()
    write1(11111)



