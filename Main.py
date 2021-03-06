from Class_Definition_ANN import ANN
from sklearn.datasets import load_boston

boston=load_boston()

print("Please initialize the state of your neurons, the synaptic weights and the network biases before continue")

print("Program now initialize the network with default setting")

"""initialize network settings"""
network_depth=10			#set the depth of this network

network_width=len(boston.data[0])

alpha=0.01

target_var=1

x=ANN(network_depth,network_width,target_var, alpha)

for i in range(network_depth):
	for j in range(network_width):
		x.Neu_hidden[i][j].initialize_synaptic_weight([0.02 for k in range(network_width)])
		x.Neu_hidden[i][j].initialize_bias(0.02)
		
for i in range(target_var):
	x.Neu_output[i].initialize_synaptic_weight([0.02 for k in range(network_width)])
	x.Neu_output[i].initialize_bias(0.02)
"""initialize network setting"""


for m in range(40):
	for n in range(len(boston.data)):
		"""prepare training examples"""
		training_example=boston.data[n]

		target_output=[boston.target[n]]

		input_signal=training_example
		"""push training examples"""

		x.receive(input_signal,target_output)	#load input stream and target output into the network

		x.feed_forward()

		x.backpropagation()

		x.update_network_weight()
		
		print(x.Neu_hidden[0][0].weight[0])
