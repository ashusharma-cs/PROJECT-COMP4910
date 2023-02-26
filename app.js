const express = require("express");
const bodyParser = require('body-parser')
const ejs= require("ejs");
let {PythonShell} = require('python-shell')
const app = express();


app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

const mongoose  = require("mongoose");
mongoose.set('strictQuery', false);
// mongoose.connect(process.env.MONGO_URL);
mongoose.connect("mongodb+srv://user_ashu:ashu@cluster1.hfx5czb.mongodb.net/tweetdatabase",{useNewUrlParser: true});


//HOME ROUTE
app.get("/",(req,res)=>{
    res.render("index.ejs");

})


// CONNECTION BETWEEN PYTHON SCRIPT AND NODEJS
let api="";
PythonShell.run('mainjson.py', null).then(messages=>{
    api= require("./alltweets_filtered_keyword_relevant.json")
  });


// JSON DATA ROUTE
app.get("/service",(req,res)=>{
    res.send(api);
})


//DATABASE SCHEMA
const tweetSchema = {
    id:Number,
    date: String,
    user: String,
    rawContent: String,
    lang: String,
    hashtags: String,
    replyCount: Number,
    user_ID: Number,
    location: String
}

//CREATING A MODEL FOR OUR DATABASE
const Tweet= mongoose.model("tweets", tweetSchema);


// A QUERY TO FIND ALL TWEETS
Tweet.find((err,tweets)=>{
    if(err)
    {
        console.log(err);
    }
    else
    {
        for (let i = 0; i < 2; i++) {
            console.log(tweets[i].rawContent);
        }
        
    }
        
    
})

// newTweet.save()



//LISTENING ON PORT 3000
app.listen(3000, function(){
    console.log("Server Started.");
})