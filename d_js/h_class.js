class Person{
    //public filed
    name;
    //private filed
    #gender;
    //static
    static species = "mamalia"
    //상수 : 변수명을 대문자로 써서 표현하는 것으로 약속
    HABIT = "earth";
    
    constructor(name, gender){
        this.name = name;
        this.#gender = gender;
    }

    get gender(){
        return this.#gender
    }

    set gender(arg){
        this.#gender = arg;
    }

    info(){
        console.log(`${this.name}:${this.gender}`);
    }

}

let hmd =new Person("name", "gender");
console.dir(hmd);
console.dir(hmd.name);
console.dir(hmd.gender);

class Employee extends Person{
    #major
    constructor(name, gender, major){
        super(name, gender);
        this.#major = major
    }
    get major(){
        return this.#major
    }
    set major(arg){
        this.#major = major
    }
}

let user = new Employee("user", "man", "lec");
console.dir(user)

console.dir(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
console.dir(user.__proto__)

user.__proto__ = {m:'프로도'}
console.dir(user.m)