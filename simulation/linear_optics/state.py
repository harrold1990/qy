import numpy as np

def ket(term): return '|%s>' % (''.join(map(str, term)))

class state:
    def __init__(self, basis):
        self.nphotons=basis.nphotons
        self.nmodes=basis.nmodes
        self.basis=basis
        self.iterator_index=0

        # A list of indeces of nonzero terms in the state vector
        self.nonzero_terms=set()
        self.vector=np.zeros(self.basis.hilbert_space_dimension, dtype=complex)

    def add(self, probability_amplitude, label):
        ''' add a term '''
        self[label]+=probability_amplitude

    def add_by_index(self, probability_amplitude, index):
        ''' add a term '''
        self[label]+=probability_amplitude
    
    ######## BOILERPLATE ########

    def __len__(self):
        ''' Just returns the number of nonzero terms'''
        return len(self.nonzero_terms)

    def __getitem__(self, key):
        ''' Allow basic square-bracket indexing '''
        if isinstance(key, int):
            return self.vector[key]
        elif isinstance(key, list) or isinstance(key, tuple):
            return self.vector[self.basis[key]]
        else:
            raise TypeError, 'Invalid state index'

    def __setitem__(self, key, value):
        ''' Allow basic square-bracket indexing '''
        if isinstance(key, int):
            self.nonzero_terms.add(key)
            self.vector[key]=value
        elif isinstance(key, list) or isinstance(key, tuple):
            index=self.basis[key]
            self.nonzero_terms.add(index)
            self.vector[index]=value
        else:
            raise TypeError, 'Invalid state index'

    def __str__(self):
        s=''
        if len(self.nonzero_terms)==0: s+='No nonzero terms in this state'
        st=sorted(self.nonzero_terms)
        for index in st:
            a=self.vector[index]
            s+='%.2f + %.2fi  ' % (a.real, a.imag)
            if self.nphotons<10: s+='  ('+ket(self.basis.modes_from_index(index))+')'
            s+='\n'
        return s

if __name__=='__main__':
    ''' Test out the state class '''
    from basis import basis
    b=basis(5, 25)
    print 'Hilbert space dimension:', b.hilbert_space_dimension
    s=state(b)
    print 'Empty state'

    # Add a bit of probability amplitude
    s[1,2,3,4,5]+=.1
    s[2,3,4,5,6]+=.1
    s[0]+=.1
    print s
    print s[0]
    print s[1,2,3,4,5]

