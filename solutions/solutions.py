def add(a,b):
    return a+b

def squared(n):
    return n*n
    
def longestword(sentence):
    return sorted(sentence.split(" "),key=lambda x: len(x))[-1]
    
def average(lst):
    return float(sum(lst))/len(lst)

def sum_to_n(n):
    return sum(range(n+1))

def repeat_n_times(str,n):
    return str*n

def doesAppear(arr,n):
    return n in arr

def isBetween(lst):
    return (lst[1] < lst[0] < lst[2])

def lstMax(lst):
    return sorted(lst)[-1]

def sortLst(lst):
    return sorted(lst)

def numDistinct(str):
    return len(set(list(str)))

def concatAll(lst):
    return ''.join(lst)

def allLower(str):
    return str.lower()

def prodAll(lst):
    return reduce(lambda x,y: x*y, lst)

def longestwordcount(sentence):
    return len(sorted(sentence.split(" "),key=lambda x: len(x))[-1])

def twosum(lst,n):
    lst = sorted(lst)
    start = 0
    end = len(lst)-1
    while start < end:
        if lst[start] + lst[end] == n:
            return True
        elif lst[start] + lst[end] > n:
            end -= 1
        else:
            start += 1
    return False

def shorten(s):
    if len(s) < 2:
        return s
    return s[0] + str(len(s)-2) + s[-1]

def prodToN(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

def reverseArray(arr):
    # reversed by itself returns a reverse iterator
    return list(reversed(arr))

def largestDiff(arr):
    arr = sorted(arr)
    return arr[-1] - arr[0]

def insertWatermelon(str):
    return " watermelon ".join(str.split())
    
def stripWhitespace(str):
    return str.strip();

def removeVowels(str):
    for v in ['a','e','i','o','u','A','E','I','O','U']:
        str = str.replace(v,'')
    return str

def bigNumNdigits(n):
    return 10**n-1

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def howManyOdds(n):
    return n/2

def palindrome(str):
    i,j = 0,len(str)-1
    while i <= j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True
    
def numPalindrome(n):
    i,j = 0,len(str(n))-1
    while i <= j:
        if str(n)[i] != str(n)[j]:
            return False
        i += 1
        j -= 1
    return True
    
if __name__ == "__main__":
    print numPalindrome(1331)
    print numPalindrome(13531)
    print numPalindrome(12)
    print numPalindrome(100)
    # print palindrome("aaba")
    # print palindrome("abba")
    # print palindrome("abcba")
    # print palindrome("abcea")
    # print howManyOdds(6)
    # print howManyOdds(7)
    # print howManyOdds(10)
    # print fib(0)
    # print fib(1)
    # print fib(2)
    # print fib(3)
    # print fib(4)
    # print fib(5)
    # print bigNumNdigits(2)
    # print bigNumNdigits(3)
    # print removeVowels('HELLOWORLD')
    # print removeVowels('Harvard')
    # print removeVowels('LowerCase')
    #print stripWhitespace("   asdfasdf   ");
    # print insertWatermelon("Last year we used a lot of napkins at Harvard");
    # print largestDiff([1,2,3,6,4,5])
    #print reverseArray([1,2,3,4,5])
    # print prodToN(5)
    # print shorten("internationalization")
    # print twosum([1,2,3,4,5],7)
    # print twosum([3,5,7,11,15],1)
    # print add(2,3) == 5
    # print add(4,5) == 9
    # print add(0,0) == 0
    # print add(-1,-1) == -2
    # print add(-1,12) == 11
    # print squared(2)
    # print squared(-4)
    # print longestword("Last year we used a lot of napkins at Harvard")
    # print longestword("A BB CCC DDDD EEEEE OVER THE HILL")
    # print average([1,2,3,4,5,6])
    # print average([3,5,7])
    # print sum_to_n(5)
    # print sum_to_n(1)
    # print sum_to_n(3)
    # print sum_to_n(10)
    # print repeat_n_times("Hi",3)
    # print repeat_n_times("Bye",4)
    # print repeat_n_times("Whee",5)
    # print doesAppear([1,2,3,4,5,6],5)
    # print doesAppear([3,5,7],1)
    # print isBetween([1, 2, 3])
    # print isBetween([5, 4, 7])
    # print isBetween([4, 4, 5])
    # print isBetween([5, 4, 5])
    # print lstMax([4,5,6,1,2,3])
    # print lstMax([6,2,5,3,1])
    # print sortLst([4,5,6,1,2,3])
    # print sortLst([6,2,5,3,1])
    # print numDistinct("test") == 3
    # print numDistinct("unique") == 5
    # print numDistinct("aaaaa") == 1
    # print numDistinct("abcabcabcabc") == 3
    # print concatAll(['a','b','cd','def'])
    # print allLower("PIN")
    # print allLower("aBcD")
    # print prodAll([1,2,3,4,5])
    # print longestwordcount("Last year we used a lot of napkins at Harvard")
    # print longestwordcount("A BB CCC DDDD EEEEEE OVER THE HILL")
    # print longestwordcount("hello world")
    # print longestwordcount("goodbye world")
    