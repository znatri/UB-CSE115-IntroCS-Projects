// Part C (20 points) - Web Front-End and JSON

function gradePrep(){
    let exams_val = document.getElementById("le").innerHTML;
    let acts_val = document.getElementById("la").innerHTML;
    let returnVal = {"exams": exams_val , "acts": acts_val};
    return returnVal;
}