//the data we provided is contained in the xlsx data
//there will be the name of the AI and the corrosponding description
//**********************************************************************//
let data = [];

function read_and_save_xlsx_file(){ //there is the corrosponding description/name
    //first we have to read the corrosponding data
    //for that i searched how to read a exel file in js on the following page: https://www.geeksforgeeks.org/how-to-read-and-write-excel-file-in-node-js/ 
    
    //the type of the file
    const file_type = require("xlsx");
    
    //reading our exel file 
    const file = file_type.readFile("./KI-Liste.xlsx"); // "./" the path is dynamic and we only need to type the name of the file


    const sheets = file.SheetNames; //we have sheets for the exel file, cause else, it would to annoying to read the data in a elegant way

    for(let i = 0; i < sheets.length; i++){

    }

}

function reset(){ //when were reseting the data currently used to compare.
    data = [];
}

function searching(){ //when user tries to search, here we will give him tips

}