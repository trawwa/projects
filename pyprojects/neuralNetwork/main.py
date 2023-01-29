import numpy as np 


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


trainingInputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

trainingOutputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synapticWeights = 2 * np.random.random((3,1)) - 1

print("Случайные инициализирующие веса:")
print(synapticWeights)

# Метод обратного распространения
for i in range(200000):
    inputLayer = trainingInputs
    outputs = sigmoid( np.dot(inputLayer, synapticWeights) )

    err = trainingOutputs - outputs
    adjustments = np.dot( inputLayer.T, err * (outputs * (1 - outputs)) )

    synapticWeights += adjustments

print("Веса после обучения:") 
print(synapticWeights)

print("Результат после обучения:")
print(outputs)