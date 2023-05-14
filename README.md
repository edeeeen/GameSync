# GameSync
A program to sync game saves (or truly any folder) between two computers

# Usage
Run `main.py` on both the computer sending the files and the computer receiving the files. For sending enter the folder with the contents that you want to send.  Then input the IP address and the port chosen by the receiving computer.  Then on the receiving computer enter the folder that you want the files to be put into.  Pick the port (its 8080 by default) and then hit receive.  The sending computer will hit send and the program on the recieving computer will close and you're done.  

## How It Sends Files
###Example sender folder:
The sender here selects the `Darkest Dungeon II/` folder contents to send.

```./Darkest Dungeon II/
├───RedHookGameLogs
├───SaveFiles
│   └───76561199584960791
│       └───profiles
│           └───...
└───Unity
    └───...```

###Example receiver folder:
The receiver here selects the folder `MyFolder` contents to be filled by the sender.

```./MyFolder/
├───RedHookGameLogs
├───SaveFiles
│   └───76561199584960791
│       └───profiles
│           └───...
└───Unity
    └───...```

It will also create a backup called `MyFolder-back1` with the contents of the original folder.
