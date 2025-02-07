import express, { urlencoded } from "express";

const app=express()

app.use(express.json())

app.use(urlencoded({extended:true}))

app.get("/",(req,res)=>{
    res.status(200).send("Hello World!")
})


console.log("Server is running on port 3000")

    
app.listen(3000)
