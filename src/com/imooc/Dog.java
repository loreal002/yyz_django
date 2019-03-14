package com.imooc;

public class Dog {
   private String name;
   private int age;
   private String color;

    public void run(){
        System.out.println(name+"在奔跑");
        System.out.println(this);
    }
    public void eat(){
        System.out.println(age+"岁大的"+name+"在吃饭");
    }
    public void setAge(int age){
        this.age = age;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setColor(String color){
        this.color = color;
    }
    public String getName(){

        return name;
    }
    public String getColor(){
        return color;
    }
    public int getAge(){
        return age;
    }
}
