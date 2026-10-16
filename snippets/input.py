# abcde => 'abcde'
s = input()

# abcde => ['a','b','c','d','e']
s = list(input())

# 5 => 5
a = int(input())

# 1 2 => 1, 2
x,y = map(int,input().split())

# 1 2 3 4 5 ... n => ['1','2','3','4','5',...,'n']
li = input().split()

# 1 2 3 4 5 ... n => [1,2,3,4,5,...,n]
li = list(map(int,input().split()))

# FFFTFTTFF => ['FFF', 'F', '', 'FF']
li = input().split('T')