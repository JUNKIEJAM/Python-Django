c_file=open('countries.txt','a');
# a: append
# r: only read
# w: wrtie
# r+: both reading and writing

#print(c_file.readline()) #readable()
#print(c_file.readlines())

#for files in c_file.readlines():
 #   print(files)
    
#c_file.close()

c_file.write('\nThis is a new line')  #will not go to new line if not done \n
c_file.close()

