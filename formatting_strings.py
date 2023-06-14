first_name = "savneet"
middle_name = "kaur"
last_name = "kahlon"
print('%s%-12s'%(first_name,last_name))
#kahlon has 6 words so space 12 will give 6 spaces to kahlon and 6 actual spaces
#kaur has 4 words so 12 spaces will give 4 spaces to kaur and 8 actual spaces
print('%s%12s%12s'%(first_name,middle_name,last_name))
#d for integer f for float
print("%10d%13d"%(1,40))
#-12 in kahlon will give 6 spaces in right 
#12 in kahlon will give 6 spaces in left
x=1234.5678
print('%10.1f'%x)