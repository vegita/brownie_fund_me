from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def fund():
    fund_me = FundMe[-1]
    # fund_me = deploy_fund_me()
    account = get_account()
    # print(account)

    version = fund_me.getVersion()
    print(f"The current version is {version}")
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
