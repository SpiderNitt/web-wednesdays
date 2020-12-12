const config = {
    iterations: 1500,
    layers: [10],
};

const data = [
    { input: 'Agra', output: 'a' },
    { input: 'Ahmedabad', output: 'a' },
    { input: 'Bangalore', output: 'b' },
    { input: 'Bhopal', output: 'b' },
    { input: 'Dehradun', output: 'd' },
    { input: 'Darjeeling', output: 'd' },
];
  
const test = 'Delhi';
  
const network = new brain.recurrent.LSTM();
network.train(data);
const output = network.run(test);
console.log(`It starts with: ${output}`); //it starts with: d