/*在程序里，有些私有属性 也想让类外特殊的一些函数或者类进行访问，就需要用到友元的技术
友元的目的就是让一个函数或者类 访问另一个类中私有成员
友元的关键字为 friend
友元的三种实现:
全局函数做友元
类做友元
成员函数做友元*/
//1.全局函数做友元
class Building
{
	friend void GoodGay(Building* p);//Goodgay全局函数是Building好朋友，可以访问Building中私有成员
public:
	Building() 
	{
		settingroom = "客厅";
		bedroom = "卧室";
	}
public:
	string settingroom;
private:
	string bedroom;
};
void GoodGay(Building *p)
{
	cout << "访问客厅：" << p->settingroom << endl;
    cout << "访问卧室：" << p->bedroom << endl;

}
void test01()
{
	Building building;
	GoodGay(&building);

}
int main()
{
	test01();
}
