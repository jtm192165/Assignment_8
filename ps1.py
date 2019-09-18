a=input("Enter binary bit data that has to be transmitted")        #taking input from user        
count=0                                                            #declaring a variable count                   
for i in a:                                                        #intiliazing a for loop to count numbers of 1 in the entered string
   if i=='1':
       count=count+1                                               #incermenting count
l=len(a)
if (count%2)==0:                                    
    a=a+'1'                                                        #adding 1 to the end of a string if it has even number of 1's
    print('binary bit data')
    print(a)                                                       #printing new string with '1' at end 
else:
    a=a+'0'                                                        #adding 0 to the end of a string if it has even number of 1's                        
    print('binary bit data')
    print(a)                                                        #printing new string with '0' at end
replace = a.replace('010', '0100')                                   #replace funtios find '010' in string and replace it with '0100'
replace = replace+'0101'
print('Transmitting data')
print(replace)                                                      #printing final required string
