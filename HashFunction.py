import numpy as np

def hash_fn(inp):
    out = np.zeros([50,len(inp)])
    print 'Example input:',
    for v in range(0,len(inp)):
        print inp[v],
    print " "
    i = 0
    j = 0
    while i<len(inp):        
        a = inp[i] % 50
        if out[a,j] == 0:
            out[a,j] = inp[i]
        else:
            while out[a,j] != 0:                
                j+=1
            if out[a,j-1] != inp[i]:
                out[a,j] = inp[i]
            j=0                  
        i += 1
    print 'Example output:'
    for m in range(0,50):
        print "%d:"%m,
        for n in range(0,len(inp)):         
            if out[m][n] != 0:
                print "%d"%(out[m][n]),
        print " "
        
inp =[5,1,2,55,8,2,105,3,100]           #example input
input = hash_fn(inp)
