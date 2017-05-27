import subprocess
text = '"Sophie. You are not being nice"'
subprocess.call('espeak '+text, shell=True)


