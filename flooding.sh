#!/bin/bash
    
FROM_ADDRESS="1W9PsEn5en4yjYd5SU2vTM5nFNshgnE5oLHyyR" 
TO_ADDRESS="1NLhXzC5SRS7eiLt4ETjRKKPQiPBo3daqw8Kpj" 
ASSET_NAME="TestAsset"          
AMOUNT=1
NUM_TRANSACTIONS=10000

for (( i=1; i<=NUM_TRANSACTIONS; i++ ))
do
    echo "Sending transaction"
    multichain-cli chain1 sendassetfrom $FROM_ADDRESS $TO_ADDRESS $ASSET_NAME $AMOUNT
    sleep 1
done

echo "Completed."