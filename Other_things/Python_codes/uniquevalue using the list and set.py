##unique and list the values using set
#set means ,it number are repeated it will store once only in set
#taking inuts are list1 & list2

def unique(list1):
    
    unique_set =set(list1)
    unique_list= list(unique_set)
    for x in unique_list:
         print (x) ,
         
list1 =[10, 20, 10, 30, 40, 40]
print ("the unique values from 1st l")
unique(list1)


         
         