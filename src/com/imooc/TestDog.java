package com.imooc;

public class TestDog {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.setAge(7);
        dog.setColor("黄色");
        dog.setName("大bai");
        dog.eat();
        dog.run();
        System.out.println("年龄是"+dog.getAge());
        System.out.println(dog);

    }

}

