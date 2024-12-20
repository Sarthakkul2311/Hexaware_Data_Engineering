lis = [0,1,2,3,4,5,6,7,8,9]
final_list = list(filter(map(lambda x :(x%2 !=0),lis)))
                
print(final_list)