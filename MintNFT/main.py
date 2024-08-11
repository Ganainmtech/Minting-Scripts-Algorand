import os
import json
import hashlib
from dotenv import load_dotenv
from algokit_utils.beta.algorand_client import AlgorandClient, AssetCreateParams
import algokit_utils
from algosdk import account, mnemonic

def generate_new_account():
    # Generate a new Algorand account
    acct = account.generate_account()
    address = acct[1]
    mnemonic_phrase = mnemonic.from_private_key(acct[0])
    return address, mnemonic_phrase

def write_mnemonic_to_env(mnemonic_phrase):
    # Write the mnemonic to a .env file for safekeeping
    with open('.env', 'w') as f:
        f.write(f"PASSPHRASE=\"{mnemonic_phrase}\"\n")

def load_passphrase_from_env():
    # Load passphrase (mnemonic) from the .env file
    load_dotenv()
    passphrase = os.getenv("PASSPHRASE")
    return passphrase

def connect_to_algorand_testnet():
    # Connect to Algorand Testnet
    algorand = AlgorandClient.test_net()
    return algorand

def get_account_from_passphrase(passphrase):
    # Retrieve the account using the provided passphrase
    account_info = algokit_utils.get_account_from_mnemonic(passphrase)
    return account_info

def load_metadata_from_file(file_path):
    # Load metadata JSON file
    with open(file_path, "r") as f:
        metadata_json = json.load(f)
    metadata_str = json.dumps(metadata_json)
    return metadata_str

def create_metadata_hash(metadata_str):
    # Create metadata hash using sha512_256
    hash_object = hashlib.new("sha512_256")
    hash_object.update(b"arc0003/amj")
    hash_object.update(metadata_str.encode("utf-8"))
    metadata_hash = hash_object.digest()
    return metadata_hash

def create_nft_asset(algorand, account, metadata_hash):
    # Create and send a transaction to create the NFT asset
    sent_txn = algorand.send.asset_create(
        AssetCreateParams(
            sender=account.address,
            signer=account.signer,
            total=1,  # Total number of tokens (1 for NFT)
            asset_name="TBA",  # Asset name (to be determined)
            unit_name="TBA",  # Unit name (to be determined)
            manager=account.address,
            clawback=account.address,
            freeze=account.address,
            url="TBA",  # URL to the metadata file on IPFS or similar
            metadata_hash=metadata_hash,
            decimals=0  # Decimals (0 for NFT)
        )
    )
    return sent_txn

if __name__ == "__main__":
    # Check if mnemonic already exists in the .env file
    passphrase = load_passphrase_from_env()

    if passphrase is None:
        # Generate new account and write mnemonic to .env file
        address, mnemonic_phrase = generate_new_account()
        print("Account Address:", address)
        write_mnemonic_to_env(mnemonic_phrase)
        print("Mnemonic saved to .env file.")
        account_info = get_account_from_passphrase(mnemonic_phrase)
    else:
        print("Mnemonic already exists in .env file. Using existing account.")
        account_info = get_account_from_passphrase(passphrase)
        address = account_info.address

    # Connect to Algorand Testnet
    algorand_client = connect_to_algorand_testnet()
    print("Connected to Algorand Testnet.")

    # Retrieve account information
    print("Account private key:", account_info.private_key)

    # Load metadata from file
    metadata_file_path = os.path.dirname(os.path.realpath(__file__)) + '/metadata.json'
    metadata_str = load_metadata_from_file(metadata_file_path)
    print("Loaded metadata:", metadata_str)

    # Create metadata hash
    metadata_hash = create_metadata_hash(metadata_str)
    print("Metadata hash:", metadata_hash)

    # Create NFT asset
    sent_transaction = create_nft_asset(algorand_client, account_info, metadata_hash)
    asset_id = sent_transaction["confirmation"]["asset-index"]
    print("NFT Asset ID:", asset_id)
