import yaml

stream = open('parameters.yaml', 'r')
data = yaml.load(stream) 

data['wheels']['diameter'] = 9.0

with open('parameters.yaml', 'w') as yaml_file:
	yaml_file.write( yaml.dump(data, default_flow_style=False))
