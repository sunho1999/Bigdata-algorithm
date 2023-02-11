import random
from tqdm import tqdm
import  matplotlib.pyplot as plt
class Bucket:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __repr__(self):
        return f"({self.start},{self.end})"

class Dgim():
    def __init__(self):
        self.bucket_tower = [[]]

    def put(self,bits):
        self.bucket_tower[0].insert(0,bits)
        layer = 0
        while len(self.bucket_tower[layer]) > 2:
            if len(self.bucket_tower) < layer + 2:
                self.bucket_tower.append([])
            if type(self.bucket_tower[layer][-1]) is list: # layer[-1]이 list일 때
                if type(self.bucket_tower[layer][-2]) is  list: # layer[-2]이 list일 때
                    if sum(self.bucket_tower[layer][-1]) + sum(self.bucket_tower[layer][-2]) <= (2**(layer+1)): # 2^b보다 작을때 2개를 올림
                        a1 = self.bucket_tower[layer].pop()
                        a2 = self.bucket_tower[layer].pop()
                        self.bucket_tower[layer + 1].insert(0, a1)
                        self.bucket_tower[layer + 1].insert(0, a2)
                    else:  # 2^b 보다 클때 1개만 올림
                        a1 = self.bucket_tower[layer].pop()
                        self.bucket_tower[layer + 1].insert(0, a1)

                elif type(self.bucket_tower[layer][-2]) is int: # layer[-2]이 int일 때
                    if sum(self.bucket_tower[layer][-1]) + self.bucket_tower[layer][-2] <= (2 ** (layer + 1)):  # 2^b보다 작을때 2개를 올림
                        a1 = self.bucket_tower[layer].pop()
                        a2 = self.bucket_tower[layer].pop()
                        a1.insert(0,a2)
                        self.bucket_tower[layer + 1].insert(0, a1)
                    else:  # 2^b 보다 클때 1개만 올림
                        a1 = self.bucket_tower[layer].pop()
                        self.bucket_tower[layer + 1].insert(0, a1)

            elif type(self.bucket_tower[layer][-1]) is int: # layer[-1]이 int일 때
                if type(self.bucket_tower[layer][-2]) is list:
                    if self.bucket_tower[layer][-1] + sum(self.bucket_tower[layer][-2]) <= (2**(layer+1)): # 2^b보다 작을때 2개를 올림
                        a1 = self.bucket_tower[layer].pop()
                        a2 = self.bucket_tower[layer].pop()
                        a2.append(a1)
                        self.bucket_tower[layer + 1].insert(0, a2)
                    else:  # 2^b 보다 클때 1개만 올림
                        a1 = self.bucket_tower[layer].pop()

                        self.bucket_tower[layer + 1].insert(0, a1)

                elif type(self.bucket_tower[layer][-2]) is int:
                    if self.bucket_tower[layer][-1] + self.bucket_tower[layer][-2] <= (2**(layer+1)): # 2^b보다 작을때 2개를 올림
                        a1 = self.bucket_tower[layer].pop()
                        a2 = self.bucket_tower[layer].pop()
                        self.bucket_tower[layer + 1].insert(0, [a1, a2])
                    else:  # 2^b 보다 클때 1개만 올림
                        a1 = self.bucket_tower[layer].pop()
                        self.bucket_tower[layer + 1].insert(0, a1)
            layer +=1
dgim = Dgim()

bitstream = [2,1,3,5,1,2,2,11,12,7]

"""for i in range(10000):
    for j in range(random.randint(0,15)):
        bitstream.append(j)"""

for b in tqdm(bitstream):
    dgim.put(b)


idx = [0]
summ = [0]
# len a = (0~7)
b = 0
id = 0
for k in range(len(dgim.bucket_tower)):
    for i in range(len(dgim.bucket_tower[k])):
        if type(dgim.bucket_tower[k][i]) is int:
            b +=1
            idx.append(b)
            c = summ[-1]
            c = c + dgim.bucket_tower[k][i]
            summ.append(c)
        elif type(dgim.bucket_tower[k][i]) is list:
            if len(dgim.bucket_tower[k]) == 1:
                idx.append(b +len(dgim.bucket_tower[k][i]))
                b += len(dgim.bucket_tower[k][i])
                c = summ[-1]
                c = c + sum(dgim.bucket_tower[k][i])
                summ.append(c)
                continue
            elif len(dgim.bucket_tower[k]) == 2:
                idx.append(b + len(dgim.bucket_tower[k][i]))
                b += len(dgim.bucket_tower[k][i])
                c = summ[-1]
                c = c + sum(dgim.bucket_tower[k][i])
                summ.append(c)


answer = [0]
id = 1
for k in range(1,100):
    if idx[id] == k:
        answer.append(summ[id])
        id +=1
    else:
        next = idx[id]
        before = idx[id-1]
        next_sum = summ[id]
        before_sum = summ[id-1]
        rest = next-before
        rest_sum = next_sum - before_sum
        rest_sum = (1- (idx[id]-k)/rest) * rest_sum
        answer.append((round(summ[id-1] + rest_sum)))


print(answer)
print(summ)

print(len(answer))

