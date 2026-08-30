// Implement Inheritance Types using JavaScript


// 1. Single Inheritance

class Animal {
    eat() {
        console.log("Animal can eat");
    }
}

class Dog extends Animal {
    bark() {
        console.log("Dog can bark");
    }
}

console.log("----- Single Inheritance -----");

let dog = new Dog();
dog.eat();
dog.bark();


// 2. Multilevel Inheritance

class Grandparent {
    house() {
        console.log("Grandparent has a house");
    }
}

class Parent extends Grandparent {
    car() {
        console.log("Parent has a car");
    }
}

class Child extends Parent {
    bike() {
        console.log("Child has a bike");
    }
}

console.log("\n----- Multilevel Inheritance -----");

let child = new Child();
child.house();
child.car();
child.bike();


// 3. Hierarchical Inheritance

class Vehicle {
    start() {
        console.log("Vehicle can start");
    }
}

class Car extends Vehicle {
    drive() {
        console.log("Car is driving");
    }
}

class Bike extends Vehicle {
    ride() {
        console.log("Bike is riding");
    }
}

console.log("\n----- Hierarchical Inheritance -----");

let car = new Car();
car.start();
car.drive();

let bike = new Bike();
bike.start();
bike.ride();


// 4. Multiple Inheritance using Mixins

let CanEat = {
    eat() {
        console.log("Human can eat");
    }
};

let CanWalk = {
    walk() {
        console.log("Human can walk");
    }
};

class Human {
    speak() {
        console.log("Human can speak");
    }
}

Object.assign(Human.prototype, CanEat, CanWalk);

console.log("\n----- Multiple Inheritance -----");

let person = new Human();
person.eat();
person.walk();
person.speak();