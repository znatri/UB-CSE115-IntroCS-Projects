// // JS OBJECTS

// let a = {'fname' : 'Hardik', 'lname' : 'Goel', 'age' : '19', 'nationality' : 'India'};
// console.log(a.fname);
// // console.log(a['fname']);
// a['fname'] = 'zNatri'
// console.log(a.fname);
// a.fname = 'Hardik';
// console.log(a.fname);
// // Remove key and its value
// delete a.fname
// // delete a['fname']
// console.log(a.fname);
// // Check if key exists
// 'fname' in a
// // !('fname' in a)

// function countMappings(obj, val){
//     let count = 0;
//     for (let v of Object.values(obj)){
//         if (v == val){
//             count += 1;
//         }
//     }
//     console.log(count)
// }

// let b = {
//   'obj1' : 'cse',
//   'obj2' : 'cse',
//   'obj3' : 'mth'
// };
// countMappings(b, 'cse');

// // for in
// let myList = ['dog', 'cat', 'bear', 'rabbit', 'tiger'];
// for (let index in myList){
//     console.log(myList[index]);
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

// // function dnaFrequency(seq){
// //     let base = ['A', 'C', 'G', 'T'];
// //     let final;
// //     for (let c of base){
// //       final.push(dnaCount(seq, c));
// //     }
// //     console.log(final);
// // }

// // dnaFrequency(mylist);

// function print_list(a){
//     for (let index of a){
//         console.log(index);
//     }
// }

// print_list(['hardik', 'goel']);

// function list_sum(a){
//     let sum = 0;
//     for (let index of a){
//         sum = sum + index;
//     }
//     return sum;
// }

// function list_concat(a){
//     let string = '';
//     for (let index of a){
//         string = string + index;
//     }
//     return string;
// }

// function indexed_list(a){
//     let nenewList;
//     for (let x in a){
//         newList;
//     }
//     return newList;
// }

// console.log(indexed_list(['1', '2', '3']));

