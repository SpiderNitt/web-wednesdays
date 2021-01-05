let $ = require('jquery');
const data= require('./data.js');
import "./additional.js";

$('#btn').click(()=>{
    data.count+=1;
    $('#data').text(data.count);
})
 console.log("Webpack");