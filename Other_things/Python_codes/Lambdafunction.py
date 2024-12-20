# Lambda function to convert a string to lowercase
string1 = 'HEXAWARE'
lower = lambda string: string.lower()
print(lower(string1))  # This will print "hexaware"

# Creating a list of lambda functions that multiply by 10
is_event_list = [lambda arg=x: arg * 10 for x in (1, 5)]
for item in is_event_list:
    print(item())  # This will print 10 and then 50
