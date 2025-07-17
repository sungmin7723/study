while(True):
    words = input()
    count = 0
    if words == "#":
        break
        
    for word in words:
        if word.lower() in ['a','i','o','u','e']:
            count += 1
    
    print(count)
