'''
Title     : Finding the percentage
Subdomain : Data Types
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    student_marks[query_name]=sum(student_marks[query_name])/3
    #map(float,student_marks[query_name])
    print '%.2f'%(student_marks[query_name])

