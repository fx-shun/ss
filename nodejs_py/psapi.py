import sys, json, numpy as np, time
     

def main():
    line = json.loads(sys.stdin.readline())
    while line:         
        np_line = np.array(line)
        #for l in np_line:         
        #    print "N: %s" % (l)
        #    sys.stdout.flush()``
        sys.stdout.write("Sum of %s = " % line)

        lines_sum = np.sum(np_line)
        
        sys.stdout.write("%d" %lines_sum)
        sys.stdout.flush()
        line = json.loads(sys.stdin.readline())

if __name__ == '__main__':
    main()

