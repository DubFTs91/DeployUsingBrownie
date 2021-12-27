from brownie import accounts, config, MyStorage, network


def deploy_my_storage():
    # Using default Ganache Account
    # account = accounts[0]

    # For Real Acct
    # Using Brownie Accounts
    # Pre Requirement. Terminal brownie accounts new account-name
    # account = accounts.load("dubRinkby-account")

    # for test Acct
    # env variable
    # account = accounts.add(config["wallets"]["from_key"])

    # print(account)

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
    deploy_my_storage()
