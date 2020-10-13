const mongoose = require('mongoose');
const User = require( './user.js');

// SET UP Mongoose Promises.
mongoose.Promise = global.Promise;
const models = {
User
}

const startDB = ({url, db }) => mongoose.connect(`mongodb://${url}/${db}`);
module.exports = {startDB,models} 
