#!/bin/bash

#Initialization
initCount=0
logs=/home/c300/logs.txt #Change the [username] path with your username without square brackets

#Telegram temporary message
message=/tmp/message.txt

#Chat id and bot telegram token
chat_id="1234563034"
token="5597026709:AAFSbxaZz0IwoWzNZyjhe7xwBZpRHiabI9A"

#Send Alert Function
function sendAlert
{
        curl -s -F chat_id=$chat_id -F text="$text" https://api.telegram.org/bot$token/sendMessage
}

#Running the program
while true
do
    lastCount=$(wc -c $logs | awk '{print $1}') #getSizeFileLogs

    if(($(($lastCount)) > $initCount));
       then
        msg=$(tail -n 2 $logs) #GetLastLineLog
        echo -e "Server Time : $(date +"%d %b %Y %T")\n\n"$msg > $message
        text=$(<$message)
        sendAlert
        echo " Alert sent!"
        initCount=$lastCount
        rm -f $message
        sleep 1
    fi
    sleep 2
done
