#OC基础-《Objective-C 程序设计 第6版》

##第三章：（类、对象和方法）

@interface 类的描述和声明

@implementation 实现在接口中声明方法的实际代码，部分用于数据描述

@property 属性声明

@synthesize 编译器自动生成getter 和 setter 方法，和带有_的同名变量，现在已不用此写法，在Xcode4.4发布之后此写法已经废弃，setter 和 getter 统称为accessor方法，即访问器方法

Program 整个程序的驱动实现

类方法、实例方法

使用实例方法必须创建对应的实例对象，实例方法以符号(-)开头;
类方法是对类本身执行操作，类方法以(+)开头

- （void）setNumberator:(NSInteger) number


方    方法              方         方       参         参
法    返回               法         法       数         数
类    类型               名         含       类         名
型                          称         参       型         称

alloc 分配内存  init 初始化实例变量

延伸问题：
1.在类的.h文件中若用@interface声明了某类，未在.m中有对应的@implement会有何种情况出现
答：编译会直接崩溃
2.@property 的修饰符有哪几种，每种都对应有哪些，具体的作用是什么
