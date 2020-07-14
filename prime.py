
def count_primes(num):
    q = 0
    odd = []
    range_num = [num for num in range(1,num+1)]
    for num in range_num:
        if not num%2==0 and num>2:
            odd.append(num)
    #print(odd)
    bef_prime = [2]
    prime = []
    non_prime = []
    while q<len(odd):
        for n in range(2,odd[q]):
            if odd[q]%n==0:
                non_prime.append(odd[q])
            else:
                bef_prime.append(odd[q])
        q+=1
    else:
        for num in bef_prime:
            if num not in non_prime:
                prime.append(num)
        print(((set(prime))))

count_primes(2147483647)
