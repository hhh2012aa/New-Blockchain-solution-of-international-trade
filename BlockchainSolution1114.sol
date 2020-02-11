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
        if (sequence == 4){
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
     
    
    
