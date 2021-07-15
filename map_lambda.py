cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    flist = [0, 1]
    
    for i in range(2, n):
        flist.append(flist[i-2]+flist[i-1])
    return flist[0:n]
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
