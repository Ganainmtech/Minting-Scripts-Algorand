# 🛠️ Algorand Minting Scripts

Welcome to the **Algorand Minting Scripts** repository! Here, you’ll find everything you need to start minting your own Tokens and NFTs on the Algorand Testnet. Whether you're a seasoned blockchain developer or just getting started, this repo will help you get up and running quickly.

## 📂 Repository Structure

This repository is organized into two main directories:

- **`MintNFT/`**: Scripts for minting Non-Fungible Tokens (NFTs) on the Algorand Testnet.
- **`MintToken/`**: Scripts for minting standard Tokens on the Algorand Testnet.

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [AlgoKit](https://developer.algorand.org/algokit/?utm_source=af_employee&utm_medium=social&utm_campaign=algokit_sarajane&utm_content=download&utm_term=EME)
- Python 3.12+ 

## 🏗️ Setup

Follow these steps to get started with the Algorand Minting Scripts:

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/algorand-minting-scripts.git
cd algorand-minting-scripts
```
### 2. Setting Up Environment Variables
Before running any scripts, ensure you've set up your environment variables. This is essential for configuring your API keys, secrets, and addresses.

### 3. Minting NFTs
To mint an NFT, follow these steps:

1. Navigate to the `MintNFT/` directory:
2. Update the `nft_metadata.json` file with your NFT details (e.g., name, description, image URL).
    ```bash
    cd MintNFT
    python mint_nft.py
    ```

### 4. Minting Tokens
To mint a standard token:

1. Navigate to the `MintToken/` directory.
2. Edit the `mint_token.py` file to customize your token's details (e.g., name, total supply, decimals).
3. Run the script to mint your token:
    ```bash
    cd MintToken
    python mint_token.py
    ```

## 📝 Note for Codespaces
If you're testing these scripts on the Algorand Testnet within a Codespace, run the following command after the initial setup to ensure everything is properly configured:

```bash
sh algorand_setup.py
```
This will prepare your environment for minting NFTs and Tokens.

## 🧪 Testing on Algorand Testnet
All scripts in this repository are configured to run on the Algorand Testnet. This is a safe environment to experiment with minting without risking real assets.

Get Testnet ALGO: Use the Algorand Testnet Dispenser to get free ALGO for testing. https://bank.testnet.algorand.network/

## 🙌 Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.
If you have any issues or questions, feel free to open an issue or reach out directly.
