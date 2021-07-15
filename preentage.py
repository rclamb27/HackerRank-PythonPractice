if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = sum(student_marks[query_name])
    size = len(student_marks[query_name])
    print("{:.2f}".format(total/size, 2))
