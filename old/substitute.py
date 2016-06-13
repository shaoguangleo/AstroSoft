def substitute(in_file,out_file,old_string,new_string):
    f_in = open(in_file,'r')
    f_out = open(out_file,'w')

    while True:
        l = f_in.readline()
        if not l:
            break
        if old_string in l:
            f_out.write(new_string)
        else:
            f_out.write(l)

if __name__ == '__main__':
    substitute('makefile','makefile_test','FCOMPL=g77','FCOMPL=gfortran')
