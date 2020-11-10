const MongoClient = require("mongodb").MongoClient;
const url = "mongodb://localhost:27017/";

MongoClient.connect(url, function (error, db) {
	if (error) throw error;
	const dbo = db.db("mydb");
	const user = { name: "John", password: "helloworld" };
	const userImposter = { whatever: "doe", password: "okok" };

	//inserting user
	dbo.collection("users").insertOne(user, function (error, result) {
		if (error) throw error;
		console.log(result);
	});

	//inserting garbage user
	dbo.collection("users").insertOne(userImposter, function (error, result) {
		if (error) throw error;
		console.log(result);
	});
});
