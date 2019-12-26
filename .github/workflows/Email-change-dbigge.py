# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("cd nodetracker" + chr(13))
	crt.Screen.WaitForString(chr(27) + "]0;devops@zen-1: " + chr(126) + "/nodetracker" + chr(7) + "devops@zen-1:" + chr(126) + "/nodetracker$ ")
	crt.Screen.Send("sed -i 's/david./d/' ./config/config.json" + chr(13))
	crt.Screen.WaitForString(chr(27) + "]0;devops@zen-1: " + chr(126) + "/nodetracker" + chr(7) + "devops@zen-1:" + chr(126) + "/nodetracker$ ")
	crt.Screen.Send("node app.js" + chr(13))
	crt.Screen.Send(chr(3) + "cat .config/c" + chr(8) + chr(8) + chr(8) + chr(8) + chr(8) + chr(8) + chr(8) + "/" + chr(8) + chr(8) + "/config/config.js" + chr(8) + "on" + chr(13))
	crt.Screen.WaitForString(chr(27) + "]0;devops@zen-1: " + chr(126) + "/nodetracker" + chr(7) + "devops@zen-1:" + chr(126) + "/nodetracker$ ")
	crt.Screen.Send(chr(27) + "[A" + chr(27) + "[D" + chr(27) + "[Ds" + chr(13))

Main()
