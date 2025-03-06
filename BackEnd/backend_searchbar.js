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
// update(); //testing my code with the following method
read_from_sql();
//******************************************//
//******************************************//
//******************************************//
debugger;

function update(){
    read_and_save_xlsx_file();
    //searching(); //comparing with the actual ki_data
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
    
    app.get('/mysql', function(req, res){
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