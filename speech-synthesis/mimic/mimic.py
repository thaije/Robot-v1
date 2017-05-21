import subprocess
text = '"Hello how are you doing"'
subprocess.call('./mimic-development/mimic -t '+text+' -voice ap', shell=True)


