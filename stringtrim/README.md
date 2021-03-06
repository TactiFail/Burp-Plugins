This plugin provides a payload generator for Intruder which will trim off one character at a time from the right side of a given position.  I don't really have any particular use case in mind, but I wrote it in an attempt to determine what sort of structure some encrypted data might have by removing one character at a time and seeing what errors appear.  I wrote [a blog post](https://tactifail.wordpress.com/2018/10/05/trim-bits-get-secrets/) demonstrating the plugin use against a mocked-up version of the client application.  The PHP code from the demo is available in this directory.

To paraphrase a conversation from Van Helsing:
```
Van Helsing: Seven years and you don't know what it does?

Carl: I didn't say that. I said I don't know what it's for, what it does is [trim off one character at a time from the right side of a given position].
```

Anyway, it requires Jython so make sure you have that configured in Burp.

Oh, and it doesn't work well in the Battering Ram configuration since there are multiple positions that could be used to determine the payload ([ref](https://github.com/PortSwigger/burp-extender-api/blob/master/src/main/java/burp/IIntruderPayloadGenerator.java#L34-L37)).

Also thank you [@redteamsecure](https://twitter.com/redteamsecure) for letting me work on this on company time  <3
