//Neural Network for XOR

const network = new brain.NeuralNetwork();


network.train([
    { input: [0, 0], output: [0] },
    { input: [0, 1], output: [1] },
    { input: [1, 0], output: [1] },
    { input: [1, 1], output: [0] },
]);
  
const output = network.run([1, 0]);
  
console.log(output[0]);
