# Windows Registry `.burp` file handler

Not a Burp plugin strictly speaking, but this Windows Registry file adds nice handling of `.burp` files by allowing double-click to open projects directly, instead of having to launch Burp and then open the file from the wizard. Also adds context menu options to launch with extensions disabled, spider and scanner paused, or both.

To install, just download and double-click then accept the prompts. You'll then be able to double-click a `.burp` file to launch, or right-click and get the following options:

![Windows context menu Burp options](/windows-registry/burp-reg-demo.png?raw=true "Screenshot of Windows context menu Burp options")

- Open Burp Project (normal launch, same as double-click)
- Open Burp Project w/ options:
  - scans and spider paused (default action when running from CLI with no args)
  - extensions disabled (passes --disable-extensions and  --unpause-spider-and-scanner)
  - both of the above (passes --disable-extensions)

It's currently set to use `%ProgramFiles%\BurpSuitePro\BurpSuitePro.exe` as the executable. If you have the Community Edition or have it installed in a non-standard location, you can comment out the lines containing `=hex(2)` and uncomment the lines underneath, editing to point to your install location. Remember to escape properly!
