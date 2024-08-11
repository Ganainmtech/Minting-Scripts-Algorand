import os
from dotenv import load_dotenv
from algokit_utils.beta.algorand_client import AlgorandClient, AssetCreateParams
import algokit_utils
from algosdk import account, mnemonic

def generate_new_account():
    # Generate a new Algorand account and return the address and mnemonic
    acct = account.generate_account()
    address = acct[1]
    mnemonic_phrase = mnemonic.from_private_key(acct[0])
    return address, mnemonic_phrase

def write_mnemonic_to_env(mnemonic_phrase):
    # Save the mnemonic to a .env file for future use
    with open('.env', 'w') as f:
        f.write(f"PASSPHRASE=\"{mnemonic_phrase}\"\n")

def load_passphrase_from_env():
    # Load the mnemonic (passphrase) from the .env file
    load_dotenv()
    passphrase = os.getenv("PASSPHRASE")
    return passphrase

def connect_to_algorand_testnet():
    # Establish a connection to the Algorand Testnet
    algorand = AlgorandClient.test_net()
    return algorand

def get_account_from_passphrase(passphrase):
    # Retrieve the account's private key and address using the mnemonic passphrase
    account_info = algokit_utils.get_account_from_mnemonic(passphrase)
    return account_info

def create_asset(algorand, account):
    # Create an Algorand Standard Asset (ASA)
    sent_transaction = algorand.send.asset_create(
        AssetCreateParams(
            sender=account.address,
            signer=account.signer,
            total=10,  # Total supply of the asset
            asset_name="Name",  # Name of the asset
            unit_name="UNIT",  # Unit name of the asset
        )
    )
    return sent_transaction

if __name__ == "__main__":
    # Load or generate the mnemonic for the account
    passphrase = load_passphrase_from_env()

    if passphrase is None:
        # Generate a new account if no mnemonic is found and save it to .env
        address, mnemonic_phrase = generate_new_account()
        print("Account Address:", address)
        write_mnemonic_to_env(mnemonic_phrase)
        print("Mnemonic saved to .env file.")
        account_info = get_account_from_passphrase(mnemonic_phrase)
    else:
        # Use the existing account mnemonic
        print("Mnemonic already exists in .env file. Using existing account.")
        account_info = get_account_from_passphrase(passphrase)
        address = account_info.address

    # Connect to the Algorand Testnet
    algorand_client = connect_to_algorand_testnet()
    print("Connected to Algorand Testnet.")

    # Create a new asset on the Testnet
    sent_transaction = create_asset(algorand_client, account_info)
    asset_id = sent_transaction["confirmation"]["asset-index"]
    print("Asset ID:", asset_id)
