try:
    a = [10,20,30,10,50]
    print (a[5])
except LookupError:
    print ("Index out of bound error")
