/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    //O(1)
   for(const _ in obj) return false
   return true
};