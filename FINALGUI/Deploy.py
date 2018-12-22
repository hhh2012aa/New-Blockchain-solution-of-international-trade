import tkinter as tk
from tkinter import *
import json
import web3
from solc import compile_source
from web3.contract import ConciseContract
from web3 import Web3, EthereumTesterProvider
from web3.auto import w3
from PIL import Image , ImageTk





contract_source_code = '''
pragma solidity ^0.4.23;
contract SaleContract{
    address applicant = msg.sender;
    
    string Buyer;
    string Seller;
    string Bank;
    address addr_Buyer;
    address addr_Seller;
    uint Price;
    uint TotalValue;
    uint timeOfShipment;
    string PortOfLanding; 
    string PortOfDest; 
    string PayDetail;
    address addr_Bank;
    uint public sequence = 1;
    
    bool public BoolDeposit;
    bool public lock_all;
    bool public AlreadyPay;
    bool public AlreadyShip;
    
    uint PayBeforeShipment;
    uint PayAfterShipment;
    
    uint EditTimes;
    
    mapping (address => uint) userSeq;
    mapping (uint => string) status;
    
    
    
   constructor  (address _importer, address _exporter, address _bank )        // 建構子 發布合約時要同時設定這三個address
    {
    addr_Buyer = _importer;
    addr_Seller = _exporter;
    addr_Bank = _bank;
    userSeq[addr_Buyer]= 1;  userSeq[addr_Seller]= 2;  userSeq[addr_Bank]= 3;
    }
    
    function dispute()                                                   //買賣有爭議時才按下，銀行接管智能合約上的貨款
    { 
    require (msg.sender==addr_Seller||msg.sender==addr_Buyer);
    sequence = 0;
    }
    
    modifier IsOwner                                    //判別開狀人身分用
    {
        require (applicant == msg.sender);
        _;
    }
    
    modifier seq                                                                    //用來控制順序
    {
        require (userSeq[msg.sender]!=0 && userSeq[msg.sender]==sequence );  
        _;
    }
    
    modifier lockAll                                     //用來保證大家都確認完後信用狀無法被任何人修改
    {
        require(lock_all == false);
        _;
    }
    
      modifier IsUser                                   //判別開狀人身分用
    {
        require (msg.sender==addr_Seller || msg.sender==addr_Buyer || msg.sender==addr_Bank );
        _;
    }
    
    
      
    function getBallence()  constant returns(uint){                //取得此合約內餘額資訊
        return address(this).balance;
    }
    
    
    function setInform ( string _Buyer , string _Seller ,  uint _Price  , uint _timeOfShipment  
    , string _PortOfLanding , string _PortOfDest , string _PayDetail ,uint _PayBeforeShipment , uint _PayAfterShipment )   lockAll IsUser returns (address)
    {   require(_PayAfterShipment + _PayBeforeShipment == _Price);
        EditTimes++;
        sequence = 1;
        Buyer = _Buyer ; Seller = _Seller ; Price = _Price;
        timeOfShipment = _timeOfShipment ; PortOfLanding = _PortOfLanding ; PortOfDest = _PortOfDest ; PayDetail = _PayDetail ;
        PayBeforeShipment = _PayBeforeShipment ; PayAfterShipment = _PayAfterShipment ;
        return msg.sender;
    }
    

   
    
    
    function output() returns (string , string ,  uint , uint , string  , string , string ,uint , uint)
    {
        return (Buyer , Seller ,   Price , timeOfShipment , PortOfLanding , PortOfDest , PayDetail , PayBeforeShipment , PayAfterShipment);
    }
  
    function pay() payable                              //用來付款的函式
    {   
        require(lock_all == true);
        if (Price <= address(this).balance)
        {
            AlreadyPay = true;    
        }
         if (address(this).balance >= PayBeforeShipment)
        {
            BoolDeposit = true;    
        }
        
        
    }
    
     
    function LcApproval()  lockAll seq{           //照順序驗證合約的函式
        sequence++;
        if (sequence >=4){
            lock_all=true;
        }
    } 
    
    function finish()                              //收貨完成後按下，智能合約把貨款支付給出口出口商
    {   require(sequence == 4);
        require(msg.sender == addr_Buyer);
        require(AlreadyPay == true);
        addr_Seller.send(Price);
        
    }
    
    function arbitrate(address addrSend , uint amount)                          //銀行仲裁時使用的函式  
    {
        require(sequence == 0);
        require(msg.sender == addr_Bank);
        require(addrSend == addr_Seller || addrSend == addr_Buyer);
        require(amount <= address(this).balance);
        addrSend.transfer(amount);
    }
    
    function shipment()                                           //出口商要出貨時按下，會檢查合約是否審核完成，以及訂金是否已經支付
    {   
        AlreadyShip = true;
        require (msg.sender == addr_Seller);
        require (lock_all == true);
        require (address(this).balance >= PayBeforeShipment);
    }
    
  
}
     
    
    
'''

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:SaleContract']

# web3.py instance
# w3 = Web3(Web3.EthereumTesterProvider()) # bug, see https://github.com/ethereum/web3.py/issues/808#issuecomment-386014138
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")) # added by me

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# Instantiate and deploy contract
Greeter = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
print(contract_interface['abi'])





#window
win=tk.Tk()
win.title("發布合約")
win.geometry("600x800")
win.configure(bg='gray20')


#Label
titleLabel=Label(win,text="請輸入以下Address",font=('微軟正黑體 bold',25),fg='steelblue2',bg='gray20')
titleLabel.place(x=300,y=80,anchor=N)

Importer=Label(win,text="進口商",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
Importer.place(x=300,y=200,anchor=N)

Exporter=Label(win,text="出口商",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
Exporter.place(x=300,y=300,anchor=N)

Bank=Label(win,text="銀行",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
Bank.place(x=300,y=400,anchor=N)


#Entry
setAddr_Importer = tk.Entry(win,font=('微軟正黑體 bold',14))
setAddr_Importer.place(x=100,y=250,width=400,height=40)

setAddr_Exporter = tk.Entry(win,font=('微軟正黑體 bold',14))
setAddr_Exporter.place(x=100,y=350,width=400,height=40)

setAddr_Bank = tk.Entry(win,font=('微軟正黑體 bold',14))
setAddr_Bank.place(x=100,y=450,width=400,height=40)

def SendContract():
    tx_hash = Greeter.constructor(w3.toChecksumAddress(setAddr_Importer.get()),w3.toChecksumAddress(setAddr_Exporter.get()),w3.toChecksumAddress(setAddr_Bank.get())).transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    Info = ( "Deployed. gasUsed={gasUsed} \n ContractAddress={contractAddress}".format(**tx_receipt) ) # added by me 
    InfoLabel=Label(win,text=Info,font=('微軟正黑體 bold',10),fg='honeydew2',bg='gray20').place(x=300,y=550,anchor=N)
#Button


bt_Send=tk.Button(win,text="送出",font=('微軟正黑體 bold',20),fg='gray10',bg='SeaGreen2',command=SendContract)
bt_Send.place(x=150,y=600,width=300,height=50)


win.mainloop()