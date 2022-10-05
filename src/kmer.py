"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('agta',1)
    ['a', 'g', 't', 'a']
    
    >>> kmer('ag',3)

    
    """
    if len(x) < k:
        return None
    result = [x[i:i+k] for i in range(len(x)-(k-1))]
    return result

    ...

def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtagt',3)
    ['agt', 'gta', 'tag']

    >>> unique_kmers('ag', 3)
    
    >>> unique_kmers('aaaaaaaaaa', 1)
    ['a']
    """

    if len(x) < k: 
        return None
    result = []
    for i in range(len(x)-(k-1)):
        kmer = x[i:i+k]
        if kmer not in result:
            result.append(kmer)
    return result
    ...

def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('aaaaa',1)
    {'a': 5}

    >>> count_kmers('ag', 3)

    """
    if len(x) < k: 
        return None 
    result = {}
    for i in range(len(x)-(k-1)):
        kmer = x[i:i+k]
        if kmer not in result:
            result[kmer]=1
        else:
            result[kmer] += 1
    return result
    
    ...
