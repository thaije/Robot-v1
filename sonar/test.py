import yaml

stream = open('parameters.yaml', 'r')
data = yaml.load(stream) 

data['sonar']['trigger']

for sonar in data['sonar']['sonars']:
	print sonar['echo']
	print sonar['position']


#data['wheels']['diameter'] = 9.0

# write
#with open('parameters.yaml', 'w') as yaml_file:
#	yaml_file.write( yaml.dump(data, default_flow_style=False))
