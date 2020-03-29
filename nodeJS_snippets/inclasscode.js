// // Arrays
// let a = ['car', 'bike', 'boat'];

// function shippingCost(x){
//     let cost;
//     if (x >= 100){
//         cost = 0;
//     } else {
//         cost = x*0.1;
//     }
//     return cost;
// }

// function totalCost(n, cpi){
//     return n*cpi;
// }

// function invoiceTotal(n, cpi){
//     let final, tax, cost, shipping;
//     cost = totalCost(n, cpi);
//     tax = cost * 0.08;
//     shipping = shippingCost(cost);
//     final =  cost + tax + shipping;
//     return final;
// }

// console.log(invoiceTotal(5, 30));
// console.log(invoiceTotal(5, 20));
// console.log(invoiceTotal(10, 2.2));
// console.log(invoiceTotal(4, 0));

// function square(x) {
//     let newarray = [];
//     for (let i = 0; i < x.length; i++) {
//         let val = Math.pow((x[i]), 2);
//         newarray.push((val));
//     }
//     console.log(newarray);
// }

// square([1, 2, 3, 4, 5]);
// square([-1]);
// square([]);

// function keep_long_string(lst) {
//     let string = [];
//     for (let st of lst) {

//     }
// }

// // Objects

// let a = { 'fname': 'Hardik', 'lname': 'Goel', 'age': '19', 'nationality': 'India' };

// // Ways to call a object
// console.log(a.fname);
// console.log(a['fname']);

// // Updating Values
// a['fname'] = 'zNatri'
// console.log(a.fname);

// a.fname = 'Hardik';
// console.log(a.fname);

// // Remove key and its value
// delete a.fname
// //delete a['fname']

// // Check if key exists
// 'fname' in a
// //!('fname' in a)

// // Data as sequence
// Object.keys(a); // gives all keys of object a using for loops
// Object.values(a); // gives all values of object a using for loops

// // for of loops
// function countMappings(obj, val) {
//     let count = 0;
//     for (let v of Object.values(obj)) {
//         if (v == val) {
//             count += 1;
//         }
//     }
//     console.log(count)
// }

// let b = {
//     'obj1' : 'cse',
//     'obj2' : 'cse',
//     'obj3' : 'mth'
//   };

// countMappings(b, 'cse');


// // for in (captures the no. of index of element)
// let myList = ['dog', 'cat', 'bear', 'rabbit', 'tiger'];
// for (let index in myList){
//     console.log(mylist[index]);
// }

// // for of (captures the value/element)
// let myList = ['dog', 'cat', 'bear', 'rabbit', 'tiger'];
// for (let index of myList){
//     console.log(index);
// }


// let mylist = ['ACGTACGTACGTTAG']

// function dnaCount(seq, base){
//     let count = 0;
//     for (let c of seq){
//         if (seq[c] === c){
//             count = count + 1;
//         }
//     }
//     return count;
// }

// function dnaFrequency(seq){
//     let base = ['A', 'C', 'G', 'T'];
//     let final = [];
//     for (let c of base){
//         final = final.push(dnaCount(seq, c));
//     }
//     console.log(final);
// }

// let customerCart = {
//     "customer1" : ["product1", "product3", "product5"],
//     "customer2" : ["product1", "product2", "product4", "product6"]
// }

// let itemsList = {
//     "product1" : 1.0, "product2" : 1.0, "product3" : 1.0, "product4" : 1.0, "product5" : 1.0, "product6" : 1.0 
// }

// // return total cost of purchase by each customer summed up together
// // For each customer in carts
// //      Compute their cart
// //      Add pairing of customers to total answer
// // return answer

// function carTotals(){

// }

// function count_large(kv){
//     let count = 0;
//     for (i of kv.values()){
//         if (i > 47.61){
//             count = count + 1;
//         }
//     }
//     return count;
// }