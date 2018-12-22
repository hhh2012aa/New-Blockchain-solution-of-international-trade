import tkinter as tk
from tkinter import *
import json
import web3
from solc import compile_source
from web3.contract import ConciseContract
from web3 import Web3, EthereumTesterProvider
from web3.auto import w3
from PIL import Image , ImageTk

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")) # added by me

w3.eth.defaultAccount = w3.eth.accounts[2]

Good_abi = [{'constant': False, 'inputs': [], 'name': 'pay', 'outputs': [], 'payable': True, 'stateMutability': 'payable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'AlreadyShip', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'AlreadyPay', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'sequence', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'LcApproval', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'shipment', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'getBallence', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_Buyer', 'type': 'string'}, {'name': '_Seller', 'type': 'string'}, {'name': '_Price', 'type': 'uint256'}, {'name': '_timeOfShipment', 'type': 'uint256'}, {'name': '_PortOfLanding', 'type': 'string'}, {'name': '_PortOfDest', 'type': 'string'}, {'name': '_PayDetail', 'type': 'string'}, {'name': '_PayBeforeShipment', 'type': 'uint256'}, {'name': '_PayAfterShipment', 'type': 'uint256'}], 'name': 'setInform', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'addrSend', 'type': 'address'}, {'name': 'amount', 'type': 'uint256'}], 'name': 'arbitrate', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'BoolDeposit', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'finish', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'output', 'outputs': [{'name': '', 'type': 'string'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'uint256'}, {'name': '', 'type': 'uint256'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'uint256'}, {'name':
'', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name':
'dispute', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name':
'lock_all', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'name': '_importer', 'type': 'address'}, {'name': '_exporter', 'type': 'address'}, {'name': '_bank', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'constructor'}]



class secondpage():
    def __init__(self,root,myTitle,flag):    
        #window
        win=tk.Tk()
        win.title("仲裁介面")
        win.geometry("800x500")
        win.configure(bg='gray20')

        Mycontract = w3.eth.contract(address= ContractAddress,abi= Good_abi,)

        #Label
        enter_Addr=Label(win,text="匯入帳號",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        enter_Addr.place(x=400,y=50,anchor=N)
        #Entry
        setAddr_entry = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_entry.place(anchor=N,x=400,y=100,width=370,height=40)

        #Label
        enter_amount=Label(win,text="匯入金額",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        enter_amount.place(x=400,y=230,anchor=N)
        #Entry
        setAmount_entry = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAmount_entry.place(anchor=N,x=400,y=280,width=370,height=40)

        def arbitratefunc():
            address1 = w3.toChecksumAddress(setAddr_entry.get())
            Amount1 = int(setAmount_entry.get())
            tx_hash = Mycontract.functions.arbitrate(address1,Amount1).transact()
            w3.eth.waitForTransactionReceipt(tx_hash)
        

        #Button
        bt_Send=tk.Button(win,text="Send",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2',command = arbitratefunc)
        bt_Send.place(x=400,y=400,width=200,height=40,anchor=N)


        win.mainloop()


root=tk.Tk()
root.title("輸入合約地址")
root.geometry("400x400")
root.configure(bg='gray20')
window1=tk.IntVar(root,value=0)

#Label
InsertAdd=Label(root,text="輸入 Contract Address",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
InsertAdd.place(x=200,y=60,anchor=N)

#Entry
ContractAdd = tk.Entry(root,font=('微軟正黑體 bold',14))
ContractAdd.place(anchor=N,x=200,y=170,width=300,height=40)

#Button
def buttonClick():
    if window1.get()== 0:
        window1.set(1)
        a = str(ContractAdd.get())
        global ContractAddress 
        ContractAddress = w3.toChecksumAddress(a)
        w1 = secondpage(root,'Send',1)
        bt_Send.wait_window(w1.top)
        window1.set(0)
        
bt_Send=tk.Button(root,text="Send",font=('微軟正黑體 bold',16),fg='gray10',bg='spring green',command=buttonClick)
bt_Send.place(x=200,y=300,width=100,height=40,anchor=N)


root.mainloop()