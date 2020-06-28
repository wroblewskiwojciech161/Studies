import numpy as np

"""zadanie 1 lista6  Wojciech Wroblewski"""

"""kolummne z jedynkami dodajemy po to by zapewnic poprawne dzialanie - kolumna ta stanowi bias, dodaje przesuniecie do funkcji"""

class NeuralNetwork:
    def __init__(self, x, y, function1, function2, d_function1, d_function2):
        np.random.seed(17)
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5
        self.function1 = function1
        self.function2 = function2
        self.d_function1 = d_function1
        self.d_function2 = d_function2

    def training(self):
        for _ in range(5000):
            self.feedforward()
            self.backprop()

    def get_error(self, out):
        return np.linalg.norm(self.y - out)

    def feedforward(self):
        self.layer1 = self.function1(np.dot(self.input, self.weights1.T))
        self.output = self.function2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * self.d_function2(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.d_function1(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return 1 * (x > 0)


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


def get_test_data(x, y):
    n = NeuralNetwork(x, y, sigmoid, sigmoid, sigmoid_derivative, sigmoid_derivative)
    n.training()
    print("combination  sigmoid,sigmoid")
    print("output")
    print(n.output)
    print("calculated error")
    print(n.get_error(n.output))

    n = NeuralNetwork(x, y, relu, relu, relu_derivative, relu_derivative)
    n.training()
    print("combination  relu,relu")
    print("output")
    print(n.output)
    print("calculated error")
    print(n.get_error(n.output))

    n = NeuralNetwork(x, y, sigmoid, relu, sigmoid_derivative, relu_derivative)
    n.training()
    print("combination  sigmoid,relu")
    print("output")
    print(n.output)
    print("calculated error")
    print(n.get_error(n.output))

    n = NeuralNetwork(x, y, relu, sigmoid, relu_derivative, sigmoid_derivative)
    n.training()
    print("combination  relu,sigmoid")
    print("output")
    print(n.output)
    print("calculated error")
    print(n.get_error(n.output))


X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

print("operation - and")
y = np.array([[0], [0], [0], [1]])
get_test_data(X, y)
print("---------------\n")

print("operation - xor")
y = np.array([[0], [1], [1], [0]])
get_test_data(X, y)
print("---------------\n")

print("operation - or")
y = np.array([[0], [1], [1], [1]])
get_test_data(X, y)
print("---------------\n")

