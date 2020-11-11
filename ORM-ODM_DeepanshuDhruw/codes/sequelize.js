const Sequelize = require("sequelize");
const sequelize = new Sequelize("mydb1", "your_username", "your_password", {
	dialect: "mysql",
});

//Defining User model
const User = sequelize.define("User", {
	username: Sequelize.STRING,
	password: Sequelize.STRING,
});

sequelize.sync();

//Inserting user
User.create({
	username: "john-doe",
	password: "okbro",
	imposter: "imposter",
}).then(function (user) {
	console.log(user);
});
