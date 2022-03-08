def prime_checker(n):
    
    for num in range(1, 100):
        if n % num == 0:
            if num != 1:
                if num != n:
                    print(n, "divides evenly with", num, "so its not prime")
                    break
                else:
                    print("number must be prime")
   

prime_checker(22)