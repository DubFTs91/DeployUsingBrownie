from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]

DECIMALS = 18
INITIAL_PRICE = 2000


def get_account():

    # Account from local Ganache w/ logging in build > deployments
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    # Account for mainnet PW protected
    elif network.show_active() == "mainnet":
        return accounts.load("mainnet-eth")
    # Account for testnet
    else:
        return accounts.add(config["wallets"]["from_key"])


# Deploy mock if testing Locally
def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks. . .")
    if len(MockV3Aggregator) < 1:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(INITIAL_PRICE, "ether"), {"from": get_account()}
        )
    print("Mock Deployed")
