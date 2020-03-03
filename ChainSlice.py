def chainslice(begin, end, *seq):
    from itertools import islice
    from itertools import chain
    print(seq)
    return islice(chain(*seq), begin, end)
    
