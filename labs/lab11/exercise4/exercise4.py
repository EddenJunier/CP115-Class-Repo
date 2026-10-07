sales = int(input())
previous = sales
count = 0
record_days = 1
while sales != 0 :
    count += 1
    if sales > previous :
        record_days +=1
    previous = sales
    sales = int(input())
print(count)
print(record_days)
