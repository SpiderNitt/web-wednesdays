const mongoose = require("mongoose");
// Database Connection
mongoose.connect("mongodb://127.0.0.1:27017/mydb1", {
	useNewUrlParser: true,
	useCreateIndex: true,
	useUnifiedTopology: true,
});

//user model
const User = mongoose.model("User", {
	username: { type: String },
	password: { type: String },
});

//new user object
const newUser = new User({
	username: "john-doe",
	password: "helloworld",
	hello: "hello",
});

//inserting/saving the document in collection
newUser.save(function (error, result) {
	if (error) {
		console.log(error);
	} else {
		console.log(result);
	}
});
