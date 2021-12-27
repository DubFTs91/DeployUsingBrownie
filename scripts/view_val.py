from brownie import MyStorage, accounts, config


def read_contract():
    # -1 gets most recent deployment
    my_storage = MyStorage[-1]
    print(my_storage.retrieve())


def main():
    read_contract()
