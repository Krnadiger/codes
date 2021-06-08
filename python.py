class codes:
    """
    All usefull functions 
    """
    def isPrime(n):
        """
        Tells wheather a given number is prime or not
        """
        if n==2 or n==3: return True
        if n%2==0 or n<2: return False
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False    
        return True
    def getAllSubStrings(a):
        """
        Returns all cotinus substrings
        """
        return [a[start:end] for start in range(0,len(a)+1) for end in range(start+1,len(a)+1)]

