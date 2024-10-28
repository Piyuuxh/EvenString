def evenstring(s):
    vowels = set('aeiouuAEIOU')
    count = 0
    n = len(s)
    
    for i in range(n//2):
        if s[i] in vowels:
            count += 1

        if s[i + n//2] in vowels:
            count -= 1

    return count == 0

s = 'piyush'
print(evenstring(s))
