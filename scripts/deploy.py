from brownie import accounts, config, MyStorage, network, FundMe, MockV3Aggregator
from scripts.all_day import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENV


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    print("Deploying Contract. . .")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
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


def main():
    deploy_my_storage()
    deploy_fund_me()
