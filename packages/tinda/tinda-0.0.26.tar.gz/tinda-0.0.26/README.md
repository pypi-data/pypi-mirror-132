# tinda
#### Buggy alpha stage, Please check back later, thankyou.
 
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
import tinda

tinda.TerminalChatServer()
# once the server is running, Clients can connect to the server and begin chatting.

import tinda

tinda.TerminalChatClient()
```

```
# Local Network Audio Chat
import tinda

tinda.LocalAudioServer()
# once the server is running, Clients can connect to the server and begin chatting.

import tinda

tinda.LocalAudioClient()

```


Developed by:
Harpreet Singh © 2021
