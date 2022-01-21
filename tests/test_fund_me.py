from brownie import network, accounts, exceptions
from scripts.fund_and_withdraw import fund
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIROMENTS, get_account
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() * 2
    print(entrance_fee)
    tx = fund_me.fund(
        {
            "from": account,
            "value": entrance_fee,
            "gas_limit": 6721975,
            "allow_revert": True,
        }
    )
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        pytest.skip("only available for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts[1]
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw(
            {"from": bad_actor, "gas_limit": 6721975, "allow_revert": True}
        )
