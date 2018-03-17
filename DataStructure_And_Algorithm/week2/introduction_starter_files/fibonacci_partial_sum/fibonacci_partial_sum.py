# Uses python3
import sys
from random import randint


mem = {}


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10





def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sumall = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sumall += current

    return sumall % 10


def cfm(n):
    if n < 0:
        return 0
    if n in mem:
        return mem[n]

    k = n // 2
    if n % 2 == 0:
        mem[n] = ((cfm(k) * cfm(k)) + (cfm(k - 1) * cfm(k - 1))) % 10
    else:
        mem[n] = ((cfm(k) * cfm(k + 1)) + (cfm(k - 1) * cfm(k))) % 10

    return mem[n]


def fibonacci_sum_adv(st, end):
    sumall = 0

    for _ in range(st, end + 1):
        sumall = (sumall + cfm(_ - 1)) % 10

    return sumall % 10


def fib_pattern(st , end):
    if end - st < 60:
        return fibonacci_sum_adv(st, end)

    sumall = 0
    k = st % 60
    if k != 0:
        sumall = sumall + fibonacci_sum_adv(k, 60)

    k = end % 60
    if k != 0:
        sumall = sumall + fibonacci_sum_adv(0, k)

    tot = (end - st) - (end % 60) - (st % 60)
    tot = tot // 60

    return (sumall + fibonacci_sum_adv(0 , 60)) % 10



def stressTest():
        
    for _ in range(40):
        x = randint(1, 200)
        c1, c2 = fib_pattern(_, _ + x), fibonacci_partial_sum_naive(_, _ + x)
        if c1 == c2:
            print("YES")
        else:            
            print("NO")
    # # for _ in range(10000):
    #     c1 , c2 = fibonacci_sum_adv(_) , fibonacci_sum_adv(_ + 60) 
    #     print("{} : {}" , c1 , c2)
        # if c1 == c2:
        #     print("i->{} YES".format(_))
        # else:
        #     print("NO value 1->{} , 2->{} and i->{}".format(c1 , c2 , _))
        #     break



if __name__ == '__main__':
    mem[0], mem[1] = 1, 1
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_pattern(from_,  to))
    # stressTest()