module.exports = {
  Query: {
    users: async (parent, args, { models }) => {
      const users = await models.User.find({});
      console.log(users.slice(0,6));
      return users.slice(0,6);
    },
    user: async (parent, args, {models})=>{
      console.log();
      const user = await models.User.find({_id: args.id});
      console.log(user);
      return user;
    }
  },
  Mutation: {
    createUser: async (parent, { name, userid, password }, { models }) => {
      const Post = await models.User.findOne({ userid });

      if (Post) {
        throw new Error('Please provide a unique title.');        
      }
      
      // create a new post
      const newUser = new models.User({
        name,
        userid,
        password,
      });

      // save the post
      try {
        await newUser.save();
      } catch (e) {
        throw new Error('Cannot Save Post!!!');
      }

      return true;
    },
    updateUser: async (parent, args, { models }) => {
      try {
        const Post = await models.User.findOneAndUpdate({ userid: args.userid },args);
      } catch (error) {
        console.log(error);
      }
      const Post = await models.User.findOneAndUpdate({ userid: args.userid },args);
      return true;
    },
  },
};