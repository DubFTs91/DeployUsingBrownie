from brownie import accounts, config, network


def get_account():
    if network.show_active() == "development":
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])

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
