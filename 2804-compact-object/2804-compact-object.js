/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    //when obj is not iterable
    if(obj === null) return null
    //recursion when iteralbe obj is array
    if(Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
    if(typeof obj !== 'object') return obj

    //when obj is iterable
    const compacted = {}
    for (const key in obj){
        let value = compactObject(obj[key])
        if(Boolean(value)) compacted[key] = value
    }

    return compacted
};