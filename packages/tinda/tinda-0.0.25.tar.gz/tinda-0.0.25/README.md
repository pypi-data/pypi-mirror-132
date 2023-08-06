# tinda
#### Buggy Sub-Alpha stage, Please Check back later, thankyou.
 
## Modern wrapper for basic things. 

### Installation:

```
pip install tinda

```

## Usage:

```
from tinda import XXX   


assistant = XXX()

assistant.say('string of whatever')

assistant.image(query) #google image search of the query string

# the same works for Google, Github, Stackoverflow, Youtube, etc.
assistant.google(query)
assistant.stackoverflow(query) 

assitant.getIp() # returns private and public ip

assiatnt.getLocation() # returns location data

assistant.time() 
assistant.date()
asssistant.recordScreen() # saves output file in root directory.
assistant.speedtest() # returns internet speed test results.
```

```
# Local network Terminal Chat
from tinda import TerminalChatServer

TerminalChatServer()
# once the server is running, Clients can connect to the server and begin chatting.

from tinda import TerminalChatClient

TerminalChatClient()
```

```
# Local Network Audio Chat
from tinda import LocalAudioServer
# once the server is running, Clients can connect to the server and begin chatting.

from tinda import LocalAudioClient

LocalAudioClient()

```


Developed by:
Harpreet Singh © 2021
