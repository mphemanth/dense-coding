from struct import pack
import sys

def shift_base(ar,b):
    # creates the variable length code for each rank
    out,arg=[],int(ar)
    while arg >0:
		out.append(arg%b) # rip off digits 
		arg=arg/b
    out[-1]=out[-1]+128 # set last byte's flag for variable operation
    return out[::-1]
    
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

    




if __name__=='__main__':
	run()

