# New Blockchain solution of international trade

# Description

1.Abandon letter of credit and manage payment through smart contract
2.Work on Ethereum (Solidity)
3.Remember to switch the account when simulating differnent identity. 

# Limit 
1.Sequence (1.Importer approval 2.Exporter approval 3.Bank approval 4.LC complete )
2.PaybeforeShippment+PayAfterShippment = 

# Quick Test on Remix ide without download any file
1.Open [Remix ide]( https://ethereum.github.io/browser-solidity/#optimize=false) in your browser

2.Create a on Remix new .sol file and paste [BlockchainSolution](https://gist.githubusercontent.com/hhh2012aa/b72338cdbb2949a764acdad4ca2682a8/raw/b0382080907d8ed829aac26e4c5f2e5161684dc9/BlockchainSolution1114.sol) 

3.Compile the contract.

4.Click Run and Choose JavaScript VM environment.

5.Copy and Paste address of Importer(0xca35b7d915458ef540ade6068dfe2f44e8fa733c), Exporter(0x14723a09acff6d2a60dcdf7aa4aff308fddc160c), Bank(0x14723a09acff6d2a60dcdf7aa4aff308fddc160c)

6.Deploy the contract with Importer Account.

7.Enter the information by using setInform function.

8.Click LC approval in order (Importer -> Exporter -> Bank).

9.When sequence = 4 , contract will lock then Importer can use Pay funciton to Pay deposit.

10.When Balance = PaybeforeShippment, boolDeposit will be True and Exporter can click shipment function.

11.When good arrive importer port, impoerter should pay the rest of payment before receiving goods(PayAfterShippment).

12.After Importer receiving goods and cofirming, clock finish function and the payment will be transferred to Exporter's account.

# Dispute Process
1.When the dispute happened, importer and Exporter can click disput function
2.After dispute function being called, Bank will gain the permission to controll the balance on contract, 
Bank will be able to use arbitrate funtion to transfer money to Importer or Exporter  according to the result of arbitrate.


