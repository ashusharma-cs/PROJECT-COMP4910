const express = require("express");
const bodyParser = require('body-parser')
const ejs= require("ejs");
const app = express();


app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

const mongoose  = require("mongoose");
mongoose.set('strictQuery', false);
// mongoose.connect(process.env.MONGO_URL);
mongoose.connect("mongodb+srv://user_ashu:ashu@cluster1.hfx5czb.mongodb.net/tweetdatabase",{useNewUrlParser: true});

app.get("/",(req,res)=>{
    res.render("index.ejs");

})

const apidata= require("./test10k.json")

app.get("/service",(req,res)=>{
    res.send(apidata);
})

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

const Tweet= mongoose.model("tweets", tweetSchema);


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


app.listen(3000, function(){
    console.log("Server Started.");
})