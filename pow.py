import hashlib
import random
import time
import threading

class Node:
    def __init__(self, node_id, is_coordinator=False):
        self.node_id = node_id
        self.is_coordinator = is_coordinator
        self.state = 'idle'  
        self.block = None
        self.chain = []
        self.logs = []
        self.failed = False

    def log(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.logs.append(f"[{timestamp}] {message}")

    def mine_block(self, previous_block=None):
        prefix = '0000'
        nonce = 0
        while True:
            block_data = f"{previous_block if previous_block else 'genesis'}-{nonce}"
            hash_value = hashlib.sha256(block_data.encode()).hexdigest()
            if hash_value.startswith(prefix):
                self.state = 'proposing'  
                self.block = {
                    'previous_block': previous_block,
                    'nonce': nonce,
                    'hash': hash_value,
                    'data': f"Block from {self.node_id}"
                }
                self.log(f"Block mined by {self.node_id}: {self.block}")
                self.state = 'idle'  
                return self.block
            nonce += 1

    def validate_block(self, block):
        if block['hash'].startswith('0000'):
            self.chain.append(block)
            self.log(f"Block {block['hash']} validated by {self.node_id}")
            return True
        else:
            self.log(f"Block {block['hash']} rejected by {self.node_id}")
            return False

    def propose_block(self, block, nodes):
        for node in nodes:
            if node != self:
                self.communicate_with_node(node, block)

    def communicate_with_node(self, node, block):
        if self.failed:
            self.log(f"Node {self.node_id} failed and cannot communicate.")
            return
        
        if node.state == 'idle':
            self.log(f"Node {node.node_id} is idle. Node {self.node_id} proposes block.")
            node.state = 'accepting'
            if node.validate_block(block):
                node.state = 'accepting'
                self.log(f"Node {node.node_id} accepted block {block['hash']}")
            else:
                node.state = 'rejecting'
                self.log(f"Node {node.node_id} rejected block {block['hash']}")
        else:
            self.log(f"Node {node.node_id} is busy. Node {self.node_id} cannot communicate.")

    def simulate_failure(self):
        if random.random() < 0.2:  
            self.failed = True
            self.log(f"Node {self.node_id} failed.")

    def recover(self):
        if self.failed:
            self.failed = False
            self.state = 'idle'  
            self.log(f"Node {self.node_id} recovered.")

def start_simulation():
    nodes = [Node(node_id=i) for i in range(5)]
    coordinator = Node(node_id='coordinator', is_coordinator=True)

    genesis_block = coordinator.mine_block()
    coordinator.log(f"Genesis Block mined: {genesis_block['hash']}")

    blocks = [coordinator.mine_block(genesis_block)]

    for round in range(10):
        time.sleep(1)
        coordinator.log(f"\nSimulação da rodada {round + 1}")

        for node in nodes:
            node.simulate_failure()
            if random.random() < 0.1:  
                node.recover()

        for node in nodes:
            if node.state == 'idle' and not node.failed:
                block = node.mine_block(blocks[-1]) 
                blocks.append(block)

        for block in blocks:
            coordinator.propose_block(block, nodes)

    for node in nodes + [coordinator]:
        print(f"\nLogs do nó {node.node_id}:")
        for log in node.logs:
            print(log)

if __name__ == '__main__':
    start_simulation()
