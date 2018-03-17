# Uses python3
import sys


mem = {}


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def cfm(n):
    
    if n in mem:
        return mem[n]

    k = n // 2
    if n % 2 == 0:
        mem[n] = ( (cfm(k)*cfm(k)) + (cfm(k-1)*cfm(k-1)) ) % 10
    else:
        mem[n] = ( (cfm(k)*cfm(k+1)) + (cfm(k-1)*cfm(k)) ) % 10

    return mem[n]

def fibonacci_sum_adv(n):
    if n == 0:
        return 0
    if n <= 1:
        return n

    sum = 0;

    for _ in range(1, n + 1):
        sum = (sum + cfm(_ - 1)) % 10

    return sum % 10


def fib_pattern(n):
    if n == 0:
        return 0
        
    if n <= 1:
        return 1

    k = n // 60
    rem = n % 60;

    sum = fibonacci_sum_adv(60) * k
    sum = sum + fibonacci_sum_adv(rem)

    return sum % 10

def stressTest():
    for _ in range(10000):
        c1 , c2 = fibonacci_sum_adv(_) , fibonacci_sum_adv(_ + 60) 
        print("{} : {}" , c1 , c2)
        # if c1 == c2:
        #     print("i->{} YES".format(_))
        # else:
        #     print("NO value 1->{} , 2->{} and i->{}".format(c1 , c2 , _))
        #     break

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    mem[0], mem[1] = 1,1
    # stressTest()
    
    print(fib_pattern(n))
    # print(fibonacci_sum_naive(n))

