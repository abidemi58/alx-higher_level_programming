#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i][0:2] != "__":
            print("{}".format(names[i]))
