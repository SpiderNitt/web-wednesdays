const mysql = require("mysql");
const conn = mysql.createConnection({
	host: "localhost",
	user: "your_username",
	password: "you_password",
	database: "mydb",
});

conn.connect(function (error) {
	if (error) {
		console.log(error);
	} else {
		console.log("Connected!");
		let createUserTable =
			"CREATE TABLE IF NOT EXISTS Users(username VARCHAR(100) NOT NULL, password VARCHAR(200) NOT NULL)";
		conn.query(createUserTable, function (error, result) {
			if (error) {
				console.log(error);
			} else {
				console.log(result);
			}
		});

		//Inserting User in Users table using SQL query
		let sql =
			"INSERT INTO Users (username, password) VALUES ('john-doe', 'oomygooturulob')";
		conn.query(sql, function (error, result) {
			if (error) {
				console.log(error);
			} else {
				console.log(result);
			}
		});
	}
});
