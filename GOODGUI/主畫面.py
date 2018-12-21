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

w3.eth.defaultAccount = w3.eth.accounts[0]

Good_abi = [{'constant': False, 'inputs': [], 'name': 'pay', 'outputs': [], 'payable': True, 'stateMutability': 'payable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'AlreadyShip', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'AlreadyPay', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'sequence', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'LcApproval', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'shipment', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'getBallence', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_Buyer', 'type': 'string'}, {'name': '_Seller', 'type': 'string'}, {'name': '_Price', 'type': 'uint256'}, {'name': '_timeOfShipment', 'type': 'uint256'}, {'name': '_PortOfLanding', 'type': 'string'}, {'name': '_PortOfDest', 'type': 'string'}, {'name': '_PayDetail', 'type': 'string'}, {'name': '_PayBeforeShipment', 'type': 'uint256'}, {'name': '_PayAfterShipment', 'type': 'uint256'}], 'name': 'setInform', 'outputs': [{'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'addrSend', 'type': 'address'}, {'name': 'amount', 'type': 'uint256'}], 'name': 'arbitrate', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name': 'BoolDeposit', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'finish', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name': 'output', 'outputs': [{'name': '', 'type': 'string'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'uint256'}, {'name': '', 'type': 'uint256'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'string'}, {'name': '', 'type': 'uint256'}, {'name':
'', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': False, 'inputs': [], 'name':
'dispute', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [], 'name':
'lock_all', 'outputs': [{'name': '', 'type': 'bool'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'name': '_importer', 'type': 'address'}, {'name': '_exporter', 'type': 'address'}, {'name': '_bank', 'type': 'address'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'constructor'}]


class secondpage():
    
    



    def __init__(self,root,myTitle,flag):    
        #window
        win=tk.Tk()
        win.title("主畫面")
        win.geometry("1000x1000")
        win.configure(bg='gray20')

        

        #Label
        buyer=Label(win,text="買家",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        buyer.place(x=250,y=50,anchor=N)
        #Entry
        setAddr_buyer = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_buyer.place(anchor=N,x=250,y=90,width=300,height=40)

        #Label
        seller=Label(win,text="賣家",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        seller.place(x=250,y=140,anchor=N)
        #Entry
        setAddr_seller = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_seller.place(anchor=N,x=250,y=180,width=300,height=40)

        #Label
        item=Label(win,text="項目",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        item.place(x=250,y=230,anchor=N)
        #Entry
        setAddr_item = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_item.place(anchor=N,x=250,y=270,width=300,height=40)

        #Label
        money=Label(win,text="金額",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        money.place(x=250,y=320,anchor=N)
        #Entry
        setAddr_money = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_money.place(anchor=N,x=250,y=360,width=300,height=40)

        #Label
        time=Label(win,text="時間",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        time.place(x=250,y=410,anchor=N)
        #Entry
        setAddr_time = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_time.place(anchor=N,x=250,y=450,width=300,height=40)

        #Label
        export=Label(win,text="出貨港",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        export.place(x=250,y=500,anchor=N)
        #Entry
        setAddr_export = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_export.place(anchor=N,x=250,y=540,width=300,height=40)

        #Label
        Import=Label(win,text="到貨港",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        Import.place(x=250,y=590,anchor=N)
        #Entry
        setAddr_Import = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_Import.place(anchor=N,x=250,y=630,width=300,height=40)

        #Label
        detail=Label(win,text="其他細節",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        detail.place(x=250,y=680,anchor=N)
        #Entry
        setAddr_detail = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_detail.place(anchor=N,x=250,y=720,width=300,height=40)

        #Label
        Deposit=Label(win,text="訂金",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        Deposit.place(x=250,y=770,anchor=N)
        #Entry
        setAddr_Deposit = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_Deposit.place(anchor=N,x=250,y=810,width=300,height=40)

        #Label
        Balance=Label(win,text="尾款",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        Balance.place(x=250,y=860,anchor=N)
        #Entry
        setAddr_Balance = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_Balance.place(anchor=N,x=250,y=900,width=300,height=40)
       
        Mycontract = w3.eth.contract(address= ContractAddress,abi= Good_abi,)

        def sendInform():
            print(ContractAddress)
            tx_hash = Mycontract.functions.setInform(setAddr_buyer.get(),setAddr_seller.get(),int(setAddr_money.get()),int(setAddr_time.get()),setAddr_export.get(),setAddr_Import.get(),setAddr_detail.get(),int(setAddr_Deposit.get()),int(setAddr_Balance.get())).transact()
            w3.eth.waitForTransactionReceipt(tx_hash)
    
        def OutputInform():
            a=Mycontract.functions.output().call()
            sequence1 = Mycontract.functions.sequence().call()
            AlreadyShip1 = Mycontract.functions.AlreadyShip().call()
            BoolDeposit1 = Mycontract.functions.BoolDeposit().call()
            print(sequence1)

            pay_output = ""
            sequence_output = ""

            if(sequence1 == 0):
                sequence_output = "進入仲裁階段"
            elif(sequence1 == 1):
                sequence_output = "出口商驗證合約中"
            elif(sequence1 == 2):
                sequence_output = "進口商驗證合約中"             
            elif(sequence1 == 3):
                sequence_output = "銀行驗證合約中"
            elif(sequence1 == 4 and AlreadyShip1 == False):
                sequence_output = "合約已完成，等待運送中"
            elif(sequence1 == 4 and AlreadyShip1 == True):
                sequence_output = "運送貨物中" 

            if(BoolDeposit1 == False):
                pay_output = "等待訂金支付中"
            elif(BoolDeposit1 == True):
                pay_output = "訂金已支付"

            aa=a[0]
            bb=a[1]
            cc=str(a[2])
            dd=str(a[3])
            ee=a[4]
            ff=a[5]
            gg=a[6]
            hh=str(a[7])
            ii=str(a[8])
            ShowContract1=Label(win,font=('微軟正黑體 bold',16),anchor=W,justify='left',bg='steel blue',text="買家:"+aa+"\n\n賣家:"+bb+"\n\n金額："+cc+"\n\n時間："+dd+"\n\n出貨港："+ee+"\n\n到貨港："+ff+"\n\n其他細節："+gg+"\n\n訂金："+hh+"\n\n尾款："+ii+"\n\n交易進度："+sequence_output+"\n\n付款進度："+pay_output)
            ShowContract1.place(x=735,y=140,width=445,height=600,anchor=N)
        
        def verified():
            tx_hash = Mycontract.functions.LcApproval().transact()
            w3.eth.waitForTransactionReceipt(tx_hash)
        
        def disputefunc():
            tx_hash = Mycontract.functions.dispute().transact()
            w3.eth.waitForTransactionReceipt(tx_hash)
        def shipmentfunc():
            tx_hash = Mycontract.functions.shipment().transact()
            w3.eth.waitForTransactionReceipt(tx_hash)

        def finishfunc():
            tx_hash = Mycontract.functions.finish().transact()
            w3.eth.waitForTransactionReceipt(tx_hash)        

        #Button
        bt_Send=tk.Button(win,text="送出",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2',command = sendInform )
        bt_Send.place(x=620,y=780,width=200,height=40,anchor=N)

        bt_Check=tk.Button(win,text="驗證",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2',command = verified)
        bt_Check.place(x=620,y=840,width=200,height=40,anchor=N)

        bt_Pay=tk.Button(win,text="付款",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Pay.place(x=620,y=900,width=200,height=40,anchor=N)

        bt_Bargain=tk.Button(win,text="起爭議",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2',command = disputefunc)
        bt_Bargain.place(x=850,y=780,width=200,height=40,anchor=N)

        bt_Ship=tk.Button(win,text="出貨",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2',command = shipmentfunc)
        bt_Ship.place(x=850,y=840,width=200,height=40,anchor=N)

        bt_Receive=tk.Button(win,text="完成收費",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2',command = finishfunc)
        bt_Receive.place(x=850,y=900,width=200,height=40,anchor=N)

        #button
        bt_Show=tk.Button(win,text="顯示目前合約資訊",font=('微軟正黑體 bold',16),fg='gray10',bg='spring green',command = OutputInform)
        bt_Show.place(x=735,y=70,width=300,height=40,anchor=N)

        #label
    
        ShowContract=Label(win,font=('微軟正黑體 bold',20),bg='steel blue')
        ShowContract.place(x=735,y=140,width=445,height=600,anchor=N)

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
ContractAdd = tk.Entry(root,font=('微軟正黑體 bold',14) )
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