import random
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
        self.ts = 0

    def put(self,bits):

        if bits == 1:
            self.bucket_tower[0].insert(0,Bucket(self.ts,self.ts))

            layer = 0
            len(self.bucket_tower) < 2
            while len(self.bucket_tower[layer]) > 2: ## layer 추가하기
                if len(self.bucket_tower) <= layer + 1:
                    self.bucket_tower.append([])

                b1 = self.bucket_tower[layer].pop()
                b2 = self.bucket_tower[layer].pop()
                b1.end = b2.end

                self.bucket_tower[layer+1].insert(0,b1)
                layer +=1
        self.ts +=1

    def count(self,k):
        s = self.ts - k
        cnt = 0

        for layer,buckets in enumerate(self.bucket_tower):
            for bucket in buckets:
                if s <= bucket.start:
                    cnt += (1 << layer)
                elif s <= bucket.end:
                    cnt += (1 << layer) * (bucket.end-s +1) // (bucket.end - bucket.start +1)
                    return cnt
                else:
                    return cnt
        return  cnt

dgim = Dgim()

bitstream = []
for i in range(15):
    prob = random.random()
    for j in range(random.randint(20,50)):
        if random.random() < prob:
            bitstream.append(1)
        else:
            bitstream.append(0)

for b in bitstream:
    dgim.put(b)

for k in range(1,200):
    print(k,dgim.count(k),sum(bitstream[-k:]))
