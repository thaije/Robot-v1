# Install
- https://github.com/MycroftAI/mimic

# Usage
- Example:
-./mimic -t "Hello. Doctor. Name. Continue. Yesterday. Tomorrow." -voice ap


-Say something:
- ./bin/mimic -t "Hello. Doctor. Name. Continue. Yesterday. Tomorrow."

-List internal voices:
- ./bin/mimic -lv

-Set voice(internal):
-./bin/mimic -t "Hello" -voice slt

-Set voice(file):
-./bin/mimic -t "Hello" -voice voices/cmu_us_slt.flitevox

-Set voice(url):
-./bin/mimic -t "Hello" -voice voices/http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_us_ksp.flitevox

-Print mimic help info:
-./bin/mimic -h


#Voice types:
-Diphone voices are less computationally expensive and quite intelligible but they lack naturalness (sound more robotic). e.g. 
-./mimic -t "Hello world" -voice kal16

- clustergen voices can sound more natural and intelligible at the expense of size and computational requirements. e.g.: e.g. ./mimic -t "Hello world" -voice slt, 
-./mimic -t "Hello world" -voice ap

- hts voices usually may sound a bit more synthetic than clustergen voices, but have much smaller size. e.g.: e.g. 
- ./mimic -t "Hello world" -voice slt_hts

