# Burp-Plugins
Just what it sounds like.

## windows-registry
Not a Burp plugin strictly speaking, but this Windows Registry file adds nice handling of `.burp` files by allowing double-click to open directly, instead of having to launch Burp and then open the file from the wizard. Also adds context menu options to launch with extensions disabled, spider and scanner paused, or both.

## stringtrim
This plugin provides a payload generator for Intruder which will trim off one character at a time from the right side of a given position.

## intrudex
**Status**: Alpha. Needs some UI work and currently has placeholders for the host, port, and SSL option when sending to Intruder. Otherwise functional.

Styled *IntRudeX*, it is an interface to generate Intruder payload positions based on results from a regex. This can be helpful when the default Intruder auto-marker functionality is too broad, or the request is too large, or you just need specific control over what gets targeted.
