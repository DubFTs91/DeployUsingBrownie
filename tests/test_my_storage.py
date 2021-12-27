from brownie import MyStorage, accounts

# export ALCHEMY_PROJECT_ID=
def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    myStorage = MyStorage.deploy({"from": account})
    initial_val = myStorage.retrieve()
    expected = 0

    # Assert
    assert initial_val == expected


def test_update_storage():
    # Arrange
    account = accounts[0]
    myStorage = MyStorage.deploy({"from": account})

    # Act

    expected = 15
    storage_trans = myStorage.store(expected, {"from": account})
    storage_trans.wait(1)
    current_val = myStorage.retrieve()

    # Assert
    assert current_val == expected
