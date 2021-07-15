if __name__ == '__main__':
    dictionary = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dictionary[name] = score
    v=dictionary.values()
    second = sorted(list(set(v)))[1]
    second_lowest = []
    
    for key, value in dictionary.items():
        if value==second:
            second_lowest.append(key)
    second_lowest.sort()
    for n in second_lowest:
        print(n)
