# Discord Crypto Bot
⚠This is a work in progress project!⚠

Do not expect any stable functions, yet. 

## Idea of this project
I want to build a Discord bot, which can be used to get current information about crypto currencies.
Many platforms offer an API which will be used to get these information.  

This bot should also offer to ability to inform you regarding your coin interests. You should be able to add coins of interests 
and desired prices to be notified.

Possible commands:

Command | Short command | Description 
------------ | ---- | -----------
!price %TOKENNAME% | !p %TOKENNAME% | Get current price of token
!tokeninfo %TOKENNAME% | !ti %TOKENNAME% | Get all market information of token
!alertprice %TOKENNAME% %PRICE% | !ap %PRICE% | Sets up an alert for a token when it reaches a specific price
!alert-ath %TOKENNAME% | !aath %TOKENNAME% | Sets up an alert for a token if it reaches an all-time-high

... and many more!


## Pre-Requirements
* [Create a Discord developer app](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)
* Create a bot and token
* Add following Permissions:
    * Texting
    * ...
* Create OAuth2 Url
* Add Bot to your desired Server

## Setup
* Copy your Bot token into a file "discord_bot_token" in the directory /secrets
* docker-compose up --build
