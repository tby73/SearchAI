//the data we provided is contained in the xlsx data
//there will be the name of the AI and the corrosponding description
//**********************************************************************//
//******************************************//
//******************************************//
//******************************************//
let data_NLP = []; 
let data_Legal_Tech = [];
let data_Kreativwerkzeuge = [];
let data_Predictive_Analystic = []; 
let data_Empfehlungssysteme = [];
let data_Sprachassistenten = []; 
let data_Multimodel = []; 
let data_Game_AI = [];
let data_Code_Generation = []; 
let data_Bild_and_Video_Generation = []; 
let data_Robotik_and_Automatisierung = []; 
//******************************************//
//******************************************//
//******************************************//
let data_NLP_link = []; 
let data_NLP_name = []; 

let data_Legal_Tech_link = [];
let data_Legal_Tech_name = [];

let data_Kreativwerkzeuge_link = [];
let data_Kreativwerkzeuge_name = [];

let data_Predictive_Analystic_link = [];
let data_Predictive_Analystic_name = []; 

let data_Empfehlungssysteme_link = [];
let data_Empfehlungssysteme_name = [];

let data_Sprachassistenten_link = []; 
let data_Sprachassistenten_name = []; 

let data_Multimodel_link = []; 
let data_Multimodel_name = []; 

let data_Game_AI_link = [];
let data_Game_AI_name = [];

let data_Code_Generation_link = []; 
let data_Code_Generation_name = []; 

let data_Bild_and_Video_Generation_link = []; 
let data_Bild_and_Video_Generation_name = []; 

let data_Robotik_and_Automatisierung_link = []; 
let data_Robotik_and_Automatisierung_name = []; 

//******************************************//
//******************************************//
//******************************************//
update(); //testing my code with the following method
//read_from_sql(); //well right now its not working, so fuck it
//******************************************//
//******************************************//
//******************************************//
debugger;

function update(){
    read_and_save_xlsx_file();
    extract_data();
    //searching(); //comparing with the actual ki_data
}


function extract_data(){
    //NLP - 1
    for (let i = 0; i < data_NLP.length; i++) {
        const item = JSON.stringify(data_NLP[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_NLP_name.push(item_split_name); //saving 
        data_NLP_link.push(item_split_link); //saving
        //console.log(item_split_link);    
        //console.log(item_split_name);    
    }

    //Legal Tech - 2
    for (let i = 0; i < data_Legal_Tech.length; i++) {
        const item = JSON.stringify(data_Legal_Tech[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Legal_Tech_name.push(item_split_name); //saving 
        data_Legal_Tech_link.push(item_split_link); //saving
        //console.log(data_Legal_Tech_link[i]);    
        //console.log(data_Legal_Tech_name[i]);    
    }

    //Kreativwerkzeuge - 3
    for (let i = 0; i < data_Kreativwerkzeuge.length; i++) {
        const item = JSON.stringify(data_Kreativwerkzeuge[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Kreativwerkzeuge_name.push(item_split_name); //saving 
        data_Kreativwerkzeuge_link.push(item_split_link); //saving
        console.log(data_Kreativwerkzeuge_link[i]);    
        console.log(data_Kreativwerkzeuge_name[i]);    
    }

    //Predictive Analystic - 4
    for (let i = 0; i < data_Predictive_Analystic.length; i++) {
        const item = JSON.stringify(data_Predictive_Analystic[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Predictive_Analystic_name.push(item_split_name); //saving 
        data_Predictive_Analystic_link.push(item_split_link); //saving
        //console.log(data_Predictive_Analystic_link[i]);    
        //console.log(data_Predictive_Analystic_name[i]);    
    }

    //Empfehlungssyteme - 5
    for (let i = 0; i < data_Empfehlungssysteme.length; i++) {
        const item = JSON.stringify(data_Empfehlungssysteme[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Empfehlungssysteme_name.push(item_split_name); //saving 
        data_Empfehlungssysteme_link.push(item_split_link); //saving
        //console.log(data_Empfehlungssysteme_link[i]);    
        //console.log(data_Empfehlungssysteme_name[i]);    
    }

    //Sprachassistenten - 6
    for (let i = 0; i < data_Sprachassistenten.length; i++) {
        const item = JSON.stringify(data_Sprachassistenten[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Sprachassistenten_name.push(item_split_name); //saving 
        data_Sprachassistenten_link.push(item_split_link); //saving
        //console.log(data_Sprachassistenten_link[i]);    
        //console.log(data_Sprachassistenten_name[i]);    
    }

    //Multimodel - 7 
    for (let i = 0; i < data_Multimodel.length; i++) {
        const item = JSON.stringify(data_Multimodel[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Multimodel_name.push(item_split_name); //saving 
        data_Multimodel_link.push(item_split_link); //saving
        //console.log(data_Multimodel_link[i]);    
        //console.log(data_Multimodel_name[i]);    
    }

    //Game AI - 8 
    for (let i = 0; i < data_Game_AI.length; i++) {
        const item = JSON.stringify(data_Game_AI[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Game_AI_name.push(item_split_name); //saving 
        data_Game_AI_link.push(item_split_link); //saving
        //console.log(data_Game_AI_link[i]);    
        //console.log(data_Game_AI_name[i]);    
    }

    //Code Generation - 9 
    for (let i = 0; i < data_Code_Generation.length; i++) {
        const item = JSON.stringify(data_Code_Generation[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Code_Generation_name.push(item_split_name); //saving 
        data_Code_Generation_link.push(item_split_link); //saving
        //console.log(data_Code_Generation_link[i]);    
        //console.log(data_Code_Generation_name[i]);    
    }

    //Bild und Video Generation - 10 
    for (let i = 0; i < data_Bild_and_Video_Generation.length; i++) {
        const item = JSON.stringify(data_Bild_and_Video_Generation[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Bild_and_Video_Generation_name.push(item_split_name); //saving 
        data_Bild_and_Video_Generation_link.push(item_split_link); //saving
        //console.log(data_Bild_and_Video_Generation_link[i]);    
        //console.log(data_Bild_and_Video_Generation_name[i]);    
    }

    //Robotik und Automatisierung - 11
    for (let i = 0; i < data_Robotik_and_Automatisierung.length; i++) {
        const item = JSON.stringify(data_Robotik_and_Automatisierung[i]);
        console.log(`Lets go ${i}: ` + item);
        //our parameter: Lets go 8: {"NLP (Natural Language Processing)":"HuggingChat (Hugging Face)","__EMPTY":"https://huggingface.co/chat/"}
        const item_split_name = item.split(`"__EMPTY":`)[0]?.trim().split(`"`)[3];        
        const item_split_link = item.split(`"__EMPTY":`)[1]?.trim().split(`"`)[1];    
        data_Robotik_and_Automatisierung_name.push(item_split_name); //saving 
        data_Robotik_and_Automatisierung_link.push(item_split_link); //saving
        //console.log(data_Robotik_and_Automatisierung_link[i]);    
        //console.log(data_Robotik_and_Automatisierung_name[i]);    
    }


}
function read_and_save_xlsx_file(){ //there is the corrosponding description/name
    //lets clear the save datas, or else we will stack our items to an insanely level
    reset();

    //first we have to read the corrosponding data
    //for that i searched how to read a exel file in js on the following page: https://www.geeksforgeeks.org/how-to-read-and-write-excel-file-in-node-js/ 
    
    //the type of the file
    const file_type = require("xlsx");

    //reading our exel file 
    const file = file_type.readFile("./KI_Liste_V2.xlsx"); // "./" the path is dynamic and we only need to type the name of the file

    const sheets = file.SheetNames; //we have sheets for the exel file, cause else, it would to annoying to read the data in a elegant way

    for(let i = 0; i < sheets.length; i++){
        const temp = file_type.utils.sheet_to_json(file.Sheets[file.SheetNames[i]]);
        temp.forEach((res) => {
            switch(i){ //those names will be in german, cause the author wrote it in english
                case 0: //NLP
                    data_NLP.push(res);
                    break;
                   
                case 1: //Legal Tech
                    data_Legal_Tech.push(res);
                    break;

                case 2: //Kreativwerkzeuge
                    data_Kreativwerkzeuge.push(res);
                    break;

                case 3: //Predictive Analystic 
                    data_Predictive_Analystic.push(res);
                    break;
                
                case 4: //Empfehlungssyteme
                    data_Empfehlungssysteme.push(res);
                    break;

                case 5: //Sprachassistenten
                    data_Sprachassistenten.push(res);
                    break;
                
                case 6: //Multimodel
                    data_Multimodel.push(res);
                    break;

                case 7: //Game-AI
                    data_Game_AI.push(res);
                    break;

                case 8: //Code-Generation
                    data_Code_Generation.push(res);
                    break;
                
                case 9: //Bild- und Video-Generation
                    data_Bild_and_Video_Generation.push(res);
                    break;

                case 10: //Robotik & Automatisierung
                    data_Robotik_and_Automatisierung.push(res);
                    break;
            }
        });
    }

    //printing our data 
    console.log(data_Bild_and_Video_Generation); //here you can test, if taking the data input is working
}

function reset(){ //when were reseting the data currently used to compare.
    let data_NLP = []; 
    let data_Legal_Tech = [];
    let data_Kreativwerkzeuge = [];
    let data_Predictive_Analystic = []; 
    let data_Empfehlungssysteme = [];
    let data_Sprachassistenten = []; 
    let data_Multimodel = []; 
    let data_Game_AI = [];
    let data_Code_Generation = []; 
    let data_Bild_and_Video_Generation = []; 
    let data_Robotik_and_Automatisierung = []; 
}

function read_from_sql(){ //with the help of https://www.w3schools.com/nodejs/nodejs_mysql_select.asp 
    var mysql = require('mysql');
    var express = require('express');
    var app = express();
    
    var connection = mysql.createConnection({
        host: "localhost",
        user: "user",
        port: "3306",
        password: "password",
        database: "mysql"
    });

    console.log(connection);
    console.log("I'm in!");

    app.get('/mysql', function(req, res){
        const queryString = "SELECT * FROM your_table";
        connection.query(queryString, function(err, rows, fields){
            if(err){
                console.log("\n......\n......\n......\n......\n");
                console.log(result);
                console.log("\n......\n......\n......\n......\n");
                console.log(fields);
            }
        });
    });
}




function transfer_json_to_txt_file(json_file){
    const fs = require("fs");
    fs.writeFileSync("output.txt", json_file, "utf8");
    console.log('Text file saved as output.txt');
}

function searching(){ //when user tries to search, here we will give him tips
    const searchbar = document.getElementById("search");
    console.log(searchbar.innerText);
    //now we will compare the written thing with our data we have and give the user a valued answer
    if(searchbar.innerText != ""){
        compare(text);
    }
    else{
        console.log("FUCKING CUNT");
    }
}

function compare(text){ //here we will be, comparing the data with our searched-text
    switch(text){
        case "ads":
            break;
    }
}