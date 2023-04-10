from web3 import Web3

# rpc
w3 = Web3(Web3.HTTPProvider('https://arbitrum-one.public.blastapi.io'))

# adress and PrivateKey
account = Web3.toChecksumAddress('0xYourAccountAddress')
private_key = '0xYourPrivateKey'

contract_address = Web3.toChecksumAddress('0x67a24ce4321ab3af51c2d0a4801c3e111d88c9d9')
input_data = '0x4e71d92d'



#GAS
payload = {
    'from': account,
    'to': contract_address,
    'data': input_data
}
estimation = int(w3.eth.estimateGas(payload)*2)


# getTransactionCount
nonce = w3.eth.getTransactionCount(account)
tx = {
    'nonce': nonce,
    'to': contract_address,
    'value': 0,
    'gas': estimation,
    'gasPrice': w3.eth.gasPrice,
    'data': input_data
}

# sign
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

# hash
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# hex
print('Transaction Hash:', tx_hash.hex())
