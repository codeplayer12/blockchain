blockchain = []

def get_last_blockchain_value():
    """
    Returns the last added item to the blockhain.
    """
    return blockchain[-1]


# Add values with a function
def add_value(transaction_amount, last_transaction=[1]):
    """
    Append a new value as well as the last block chain value to the blockchain
    
    :param transaction_amount: The amount that should be added
    :param last_transaction: The last blockchain transaction(default [1])
    """
    blockchain.append([last_transaction,transaction_amount])

def get_user_input():
    """
    Returns the input of the user ( a new transaction amount) as a float.
    """
    return float(input('Your transaction amount please: '))

tx_amount = get_user_input()
add_value(tx_amount)
add_value(5.9, get_last_blockchain_value())
add_value(15, get_last_blockchain_value())

print(blockchain)