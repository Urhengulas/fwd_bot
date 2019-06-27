# fwrd_bot

> The fwrd_bot (forward_bot) is a simple bot to forward all messages, users send to the bot, to a specific group.

- [Getting started](#Getting-started)
  - [Install dependencies:](#Install-dependencies)
  - [Create a telegram bot](#Create-a-telegram-bot)
  - [Know your secrets vol. 1](#Know-your-secrets-vol-1)
  - [Run your bot](#Run-your-bot)
  - [Add bot to group](#Add-bot-to-group)
  - [know your secrets vol. 2](#know-your-secrets-vol-2)
  - [Your are done](#Your-are-done)
- [Files](#Files)

## Getting started

### Install dependencies:
```shell
make dep
```
### Create a telegram bot 
Go (in telegram) to [@botfather](https://web.telegram.org/#/im?p=@BotFather) and configure a bot. You get a `TOKEN` you will need later on.

### Know your secrets vol. 1
Create a [secret.py](./secret.py) file including the variables:

| var        | use                                | where to get it                      |
| :--------- | :--------------------------------- | :----------------------------------- |
| `TOKEN`    | the token of your bot              | from @botfather                      |
| `GROUP_ID` | the chat id of the to-fwd-to-group | just set it to `0` for the beginning |

### Run your bot
```shell
make run
```

### Add bot to group
Add that bot to the group it shall forward messages to, just like you would add a normal user.

To activate the bot send this message to the group:
```text
/start @name_of_bot 
```
It will send you a hello text and your chat id. This chat id is the `GROUP_ID`.

### know your secrets vol. 2
Add the `GROUP_ID` to your secrets.py

### Your are done
Now everyone can just send messages to your bot and these will be forwarded to your channel.

**Well done!**

## Files

| file      | use                             |
| :-------- | :------------------------------ |
| bot.py    | the bot lives here              |
| secret.py | `TOKEN`, `GROUP_ID`             |
| texts.py  | the center of poetic creativity |
