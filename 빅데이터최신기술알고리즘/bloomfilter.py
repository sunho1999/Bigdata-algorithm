import math
import mmh3
import random

class BloomFilter:
    def __init__(self,capacity,fp_prob):
        self.capacity = capacity
        self.fp_prob = fp_prob
        self.bitarray = 0
        self.n_bits = math.ceil(-math.log(fp_prob,math.e) * capacity/(math.log(2,math.e)**2))
        self.n_hashs = int(self.n_bits / capacity * math.log(2,math.e))  # k의 개수
        self.seeds = [random.randint(0,999999) for i in range(self.n_hashs)]
        print(self.n_bits)
        print(self.n_hashs)

    def put(self,item):
        for i in range(self.n_hashs):
            pos = mmh3.hash(item,self.seeds[i]) % self.n_bits
            self.bitarray |= (1 << pos)

    def test(self,item):
        for i in range(self.n_hashs):
            pos = mmh3.hash(item, self.seeds[i]) % self.n_bits

            if self.bitarray & (1 << pos) == 0:
                return False
        return True

bloom = BloomFilter(100000000,0.021577141)

bloom.put('a')
bloom.put('b')
bloom.put('c')
bloom.put('d')
bloom.put('e')
bloom.put('f')
bloom.put('g')
print('a', bloom.test('a'))
print('b', bloom.test('b'))
print('c', bloom.test('c'))
print('d', bloom.test('d'))
print('e', bloom.test('e'))
print('f', bloom.test('f'))
print('g', bloom.test('f'))
print('h', bloom.test('h'))
print('i', bloom.test('i'))
print('j', bloom.test('j'))
print('k', bloom.test('k'))
print('l', bloom.test('l'))
print('m', bloom.test('m'))
