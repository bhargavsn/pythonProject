#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example Script
# ----------- All Imports here ------------------
from time import time
from BlockChain_Hashing import custom_hash


# ------------ Class Definition Start --------
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(
            previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.",
            proof=100)

    # Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending
    # transactions & append the newest block to the chain.

    def new_block(self, proof: object, previous_hash: object = None) -> object:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or custom_hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    # Search the blockchain for the most recent block.
    @property
    def last_block(self):
        return self.chain[-1]

    # Add a transaction with relevant info to the 'blockpool' - list of pending tx's.
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1


blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(6789)

# Print the Main Chain in the Block
print("Genesis block: ", blockchain.chain, sep='\n')


