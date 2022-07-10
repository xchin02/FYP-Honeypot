# Keylogger
keylog.py - Client-side script: To log user's keystrokes and save them to a file called keylog.log. When user presses "escape" key, it exists out of the keyboard listener and connects to keylog server (attacker's server) to send log file.

keylogserver.py - Server-side script: Receives log file from victim and analyses it for malicious purposes like retrieving password information.
