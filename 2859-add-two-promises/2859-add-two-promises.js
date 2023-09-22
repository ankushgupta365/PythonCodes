/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    //above promise will get resolve after largest time of any of the below promises 
    //O(max(promise1, promise2))
    const [value1, value2] = await Promise.all([promise1, promise2])
    return value1+value2
};


//example usage of the above implementation

// const pro1 = new Promise(resolve=>setTimeout(()=>resolve(2), 20))
// const pro2 = new Promise(resolve=>setTimeout(()=>resolve(4), 40))
// addTwoPromises(pro1, pro2).then(res =>console.log(res))

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */