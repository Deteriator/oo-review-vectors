class Vec {
	constructor(x,y){
        this.x = x;
        this.y = y;
    }
    plus(vector){
        let newX = this.x += vector.x;
        let newY = this.y += vector.y;
        return new Vec(newX,newY);
    }
    minus(vector){
        let newX = this.x -= vector.x;
        let newY = this.y -= vector.y;
        return new Vec(newX,newY);
    }
    get length(){
        return Math.sqrt(Math.pow(this.x,2) + Math.pow(this.y,2));
    }
    static distance(arr1,arr2){
    	let num1 = arr2[0] - arr1[0]
    	let num2 = arr2[1] - arr1[1]
    	return Math.sqrt(num1 ** 2 + num2 ** 2)
    }
}