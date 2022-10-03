import hashlib

def hashGen(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:
    def __init__(self,data,hash,prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:
    def __init__(self):
        lastHash = hashGen('gen_last')
        startHash = hashGen('gen_hash')

        genesis = Block('gen-data',startHash,lastHash)
        self.chain=[genesis]


    def add_block(self,data):
        prev_hash = self.chain[-1].hash
        hash = hashGen(data+prev_hash)
        block = Block(data,hash,prev_hash)
        self.chain.append(block)


bc=Blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')


for block in bc.chain:
    print(block.__dict__)


