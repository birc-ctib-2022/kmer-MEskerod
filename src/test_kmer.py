# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from kmer import (
    kmer,
    unique_kmers,
    count_kmers
)


def test_kmer():
    assert kmer('agtagtagta', 6) == ['agtagt','gtagta','tagtag','agtagt','gtagta']
    assert kmer('agt', 5) == None
    assert kmer('agt',1) == ['a','g','t']


def test_uniue_kmers():
    assert unique_kmers('agta',7) == None
    assert unique_kmers ('aaaaaaaaaaa', 3) == ['aaa']
    assert unique_kmers ('agtcagtcagtc',4) == ['agtc','gtca','tcag','cagt']

def test_count_kmers():
    assert count_kmers('ag', 3) == None
    assert count_kmers('aaaa', 1) == {'a': 4}
    assert count_kmers('agtagtagt',3) == {'agt': 3, 'gta': 2, 'tag': 2}