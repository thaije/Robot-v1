import subprocess
text = '"Hello how are you doing"'
subprocess.call('espeak '+text, shell=True)


