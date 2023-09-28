/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((res,item)=>{
        const key = fn(item)
        if(!(key in res)){
            //if key not their then initialize with []
            res[key] = []
        }
        res[key].push(item)
        return res
    }, {})   //initial res
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */