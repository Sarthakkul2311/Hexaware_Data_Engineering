is_event_list = [lambda arg=x: arg*10 for x in (1, 2)]
for item in is_event_list:
 print(item())