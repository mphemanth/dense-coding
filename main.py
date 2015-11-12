from struct import pack
import sys

def shift_base(ar,b):
    # creates the variable length code for each rank
    out,arg=[],int(ar)
    print arg,arg/b

    arg=arg-(arg/b)
    print arg,arg/b

    while arg >0:
        print arg%b
        out.append(arg%b)
        #out.append(arg%b) # rip off digits 
        arg=arg/b
    out[-1]=out[-1]+128
    return out
    
def to_binary(l):
    # create binary data from list 
    #return pack('%d'%len(l)+'B',*l)
    return bytearray(l)
    

def write_file(l,f):
    # write binary data to file
    x=open(f,'wb')
    x.write(bytearray(l))
    x.close()
    
    
def run():
    d=shift_base(sys.argv[1],128) # example use 
    print d
    




if __name__=='__main__':
	run()

