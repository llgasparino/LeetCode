/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {

    let valorBaixo = 0;
    let valorAlto = nums.length -1;

    while (valorBaixo <= valorAlto) {
        meio = Math.floor((valorBaixo + valorAlto) / 2)
        valorMeio = nums[meio]

        if(target === valorMeio){

            return meio;

        } else if (target > valorMeio){

            valorBaixo = meio + 1;

        } else if (target < valorMeio){

            valorAlto = meio - 1;

        }
    } 

    return -1;
    
