def merge_the_tools(string, k):
    split_string = []
    for i in range(0, len(string), k):
        split_string.append(string[i:i+k])
    list = ""
    for z in split_string:
        for i in z:
            if i not in list:
                list += i
        print(list)
        list = ""
        
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
