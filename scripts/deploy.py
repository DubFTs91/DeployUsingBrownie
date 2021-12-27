from brownie import accounts, config, MyStorage, network, FundMe, MockV3Aggregator
from scripts.all_day import get_account


def deploy_fund_me():
    account = get_account()

    if network.show_active != "developement":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        # BUG HERE
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks. . .")
        mock_aggregator = MockV3Aggregator.deploy(
            18, 2000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print("Mock Deployed")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True,
    )
    print(f"Contract deployed to {fund_me.address}")


def deploy_my_storage():

    account = get_account()

    # initialze MyStorage
    my_storage = MyStorage.deploy({"from": account})
    current_val = my_storage.retrieve()
    print(current_val)

    storage_trans = my_storage.store(77, {"from": account})
    storage_trans.wait(1)
    current_val = my_storage.retrieve()
    print(current_val)


def get_account():
    if network.show_active() == "development":
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    # deploy_my_storage()
    deploy_fund_me()
