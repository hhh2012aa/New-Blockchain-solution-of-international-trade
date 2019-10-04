# New Blockchain solution of international trade

![image](https://github.com/hhh2012aa/55564/blob/master/44834455_1217049235110214_847730508761661440_n.png?raw=true) ![image](https://github.com/hhh2012aa/55564/blob/master/123456.png?raw=true) 
       
      

# Description

1. Replace Letter of Credit (L/C) with smart contract to manage transaction payments.

2. Smart contract programming language: Solidity.

3. Blockchain platform: Ethereum.

4. Remember to switch the account when simulating with differnent identities. 

5. [Quorum](https://github.com/jpmorganchase/quorum) is a Ethereum-based platform, which allows user to assign specific accounts to view the information or use the functions of contract before the contract is deployed.

# Certification Mechanism
1. Sequence of contract certification (1.Importer approval -> 2.Exporter approval -> 3.Bank approval -> 4.LC complete )

2. Automatic Reconciliation System  <br />
The payment (PaybeforeShippment+PayAfterShippment) should be equal to contract price so that the contract will be certificated.

# Quick Test on Remix ide without downloading any file
1. Open [Remix ide]( https://ethereum.github.io/browser-solidity/#optimize=false) in your browser

2. Create a new .sol file on Remix and paste [BlockchainSolution](https://gist.githubusercontent.com/hhh2012aa/b72338cdbb2949a764acdad4ca2682a8/raw/b0382080907d8ed829aac26e4c5f2e5161684dc9/BlockchainSolution1114.sol) 

3. Compile the contract.

4. Click Run and Choose JavaScript VM environment.

5. Copy and Paste address of Importer(0xca35b7d915458ef540ade6068dfe2f44e8fa733c), Exporter(0x14723a09acff6d2a60dcdf7aa4aff308fddc160c), Bank(0x14723a09acff6d2a60dcdf7aa4aff308fddc160c)

6. Deploy the contract with Importer Account.

7. Enter the information by using setInform function.

8. Click LC approval in order (Importer -> Exporter -> Bank).

9. After getting 3 parties approval (sequence = 4) , contract will lock then Importer can use Pay funciton to Pay deposit.

10. When Balance = PaybeforeShippment, boolDeposit will be True and Exporter can click shipment function.

11. After goods arrive importer port, importer should pay the rest of payment before receiving goods(PayAfterShippment).

12. After Importer receiving goods and cofirming, clock finish function and the payment will be transferred to Exporter's account.

# Dispute Process
1. When the dispute happened, importer and Exporter can click dispute function.

2. After dispute function being called, Bank will gain the permission to controll the balance on contract, 
Bank will be able to use arbitrate funtion to transfer money to Importer or Exporter  according to the result of arbitrate.

# Future Work
1. Python GUI (in the process)

2. Add the rest of detail to build a full-featured platform.

3. Web GUI

