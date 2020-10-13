const { GraphQLServer } = require('graphql-yoga');
const { startDB, models } = require('./db');
const resolvers = require('./graphql/resolvers');

const db = startDB({
  db: 'graphie',
  url: 'localhost:27017'
})

const context = {
  models,
  db,
};

const Server = new GraphQLServer({
  typeDefs: `${__dirname}/graphql/schema.graphql`,
  resolvers,
  context,
});

// options
const opts = {
  port: 4000,
};


Server.start(opts, () => {
  console.log(`Server is running on http://localhost:${opts.port}`);
});
