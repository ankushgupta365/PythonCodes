/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    const result = arr.sort((a,b)=>fn(a)-fn(b))
    return result
};