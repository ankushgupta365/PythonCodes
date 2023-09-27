/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
  if(this.length == []){
      return -1
  }else{
      let res = null
      for (let i =0; i<this.length; i++){
          res = this[i]
      }
      return res
  }
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */