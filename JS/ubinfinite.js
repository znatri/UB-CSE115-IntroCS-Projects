// function download_time(filesizeGB){
//     let esttime, downspeed, filesizeMb;
//     downspeed = 78;
//     filesizeMb = (filesizeGB * 1000 * 8);
//     esttime = filesizeMb / downspeed;
//     return esttime;
// }

// function hoo(){
//     console.log(Math.sin(-2.96));
// }

// function line_eval(x){
//     let y, m, c;
//     m = 0.46;
//     c = 7.98;
//     y = m*x + c;
//     return y;
//  }

// function pool_volume(h){
//     let r, vol;
//     r = 13;
//     vol = Math.PI*(r*r)*h;
//     return vol
// }

// function parabola_eval(x){
//     let y, a, b, c;
//     a = -1.81;
//     b = 2.07;
//     c = 12.23;
//     y = (a*(x*x)) + (b*x) + (c);
//     return y;
// }

// function compute_xp(xp, bool){
//     if (bool === false){
//         return 59877;
//     } else {
//         return 59877+xp;
//     }
// }

// function higher_lower(x){
//     if (x < 24){
//         return "higher";
//     } else if (x > 24){
//         return "lower";
//     } else {
//         return "correct";
//     }   
// }

// function same_side(x, y){
//     if (x > 38 && y > 38){
//         return true;
//     } else if (x < 38 && y < 38){
//         return true;
//     } else {
//         return false;
//     }
// }

// function categorize(x){
//     if (x < 23){
//         return "low";
//     } else if (x >= 23 && x < 36){
//         return "medium";
//     } else {
//         return "high";
//     }   
// }

// function replacement(yay){
//   let bru = yay.replace(/a/g, 'd');
//   return bru;
// }

// function characters(x){
//     return x.length;
// }

// characters("aa");

// function tweets(word){
//     let length = word.length;
//     text = Math.ceil(length / 280);
//     return text;
// }

// tweets("hardik ");

// let a = ['car', 'bike', 'boat'];
// console.log(a);

// function distance(x, y){
//   let p1 = 8.8;
//   let q1 = 17.5;
//   let d = Math.pow((Math.pow((x-p1),2) + Math.pow((y-q1),2)), 0.5);
//   return d;
// }
// distance(0,0);

// function count_in_range(a){
//     let count = 0;
//     for (let i of a){
//         if (i > 25.71 && i < 43.96){
//             count = count + 1;
//         }
//     }
//     return count;
// }

// function categorize(x){
//     let length = x.length;
//     if (length < 4){
//         return "short";
//     } else if (length >= 4 && length < 7){
//         return "medium";
//     } else {
//         return "long";
//     }   
// }

// function square(x){
//   let newarray = [];
//   for (let i =0; i <  x.length; i++){
//     let val = Math.pow((x[i]), 2);
//     newarray.push((val));
//   }
//   console.log(newarray);
// }

// square([1, 2, 3, 4, 5]);
// square([-1]);
// square([]);

// function find_value(a){
//     let status = 0;
//     for (let x of a){
//         if (x === 0){
//             status = status + 1;
//         } 
//     }
//     if (status > 0){
//         return true;
//     } else {
//         return false;
//     }
// }

// function count_values(a){
//     let count = 0;
//     for (let i of a){
//         if (i > 641){
//             count = count + 1;
//         }
//     }
//     return count;
// }

// function get_value(kv){
//     for (let i in kv){
//         if (i == "consistently"){
//             return kv[i];
//         }
//     }
// }

// let kv = {
//   "consistently" : 1,
//   "a" : 1,
//   "b" : 2
// };

// get_value(kv);

// function sum_values(kv){
//     let sum = 0;
//     for (let i in kv){
//         sum += kv[i];
//     }
//     return sum;
// }

// let obj1 = {
//   "consistently" : 1,
//   "a" : 1,
//   "b" : 2,
//   "c" : 9,
//   "d" : 10
// };

// function count_values_obj(kv){
//   let count = 0;
//   for (let i in Object.values(kv)){
//     if (i > 5){
//       count = count + 1;
//     }
//   }
//   return count;
// }

// function getUserInput(){
//     let element = document.getElementById("user_input");
//     return element.value;
// }

// function copyInput(){
//     let val = document.getElementById("user_input").value;
//     document.getElementById("copied_input").innerHTML = val;
// }

// function insertWord(){
//     let element = document.getElementById("content");
//     element.innerHTML = "voluntary";
// }

// function additionCalculator(){
//     let a = document.getElementById("input_one").value;
//     let b = document.getElementById("input_two").value;
//     let sum = Number(a) + Number(b);
//     document.getElementById("sum").innerHTML = sum;
// }

// function plotPie(categories){
//   let val = [];
//   let label = [];

//   for (let entry of categories){
//     val.push(entry[0]);
//     label.push(entry[1]);
//   }

//   let data = [{
//     values : val,
//     labels : label,
//     type : "pie"
//   }];

//   Plotly.newPlot('plot', data);
// }

// function plotLine(plotpoints){
//     let xval = [];
//     let yval = [];
//     for (let coord of plotpoints){
//         xval.push(coord[0]);
//         yval.push(coord[1]);
//     }
//     let data = [{
//         x : xval,
//         y : yval
//     }];
//     Plotly.newPlot('plot',data);
// }

// function get_y(blob) {
//     let data = JSON.parse(blob);
//     for (let i in data['x']) {
//         if (data['x'][i] == -2) {
//             return data['y'][i];
//         }
//     }
// }

// function json_filter(lst){
//     let dataLst = JSON.parse(lst);
//     let newList = [];
//     for (let item of dataLst){
//         if (item["mass"] > 36.77){
//             newList.push(item);
//         }
//     }
//     return JSON.stringify(newList);
// }

// function json_average(lst){
//     let dataLst = JSON.parse(lst);
//     let totalSum;
//     let count;
//     for (let item of dataLst){
//         totalSum += item["temperature"];
//         count += 1;
//     }
//     let avg_temp = totalSum/count;
//     let data = {"temperature": avg_temp};
//     return JSON.stringify(data);
// }

// Custom Sorting (due week of Apr. 20)

// function sort_list(list){
//     list.sort();
// }

// function sort_kvs(list){
//     list.sort(sort_spin);
// }

// function sort_spin(kv1, kv2){
//     if (kv1["spin"] < kv2["spin"]){
//         return -1;
//     } else if (kv1["spin"] > kv2["spin"]) {
//         return 1;
//     } else{
//         return 0;
//     }
// }

// function sort_by_length(list){
//     list.sort(string_length);
// }

// function string_length(kv1, kv2){
//     if (kv1.length < kv2.length){
//         return -1;
//     } else if (kv1.length > kv2.length) {
//         return 1;
//     } else{
//         return 0;
//     }
// }

// function sort_by_product(list){
//     list.sort(list_multiple);
// }

// function list_multiple(kv1, kv2){
//     let val1 = kv1[0] * kv1[2] ;
//     let val2 = kv2[0] * kv2[2] ;
//     if (val1 < val2){
//         return -1;
//     } else if (val1 > val2) {
//         return 1;
//     } else{
//         return 0;
//     }
// }

// function sort_by_average_rating(list){
//     list.sort(compareFn);
// }

// function compareFn(kv1, kv2){
//     let ratingsList1 = kv1.ratings;
//     let ratingsList2 = kv2.ratings;
//     let avgRatings1 = 0;
//     let avgRatings2 = 0;
//     for (let rating of ratingsList1){
//         avgRatings1 += Number(rating);
//     }
//     for (let rating of ratingsList2){
//         avgRatings2 += Number(rating);
//     }
//     avgRatings1 /= ratingsList1.length;
//     avgRatings2 /= ratingsList2.length;
//     if (avgRatings1 < avgRatings2){
//         return -1;
//     } else if (avgRatings1 > avgRatings2) {
//         return 1;
//     } else{
//         return 0;
//     }
// }