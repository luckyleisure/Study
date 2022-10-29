class building;
class goodgay
{
public:

	void visit();
	
	void visit1();
	
	goodgay();
	
	building* build;  

}; 
class building
{
	friend void goodgay::visit();
public:
	building();
public:
	string settingroom;
private:
	string bedroom;

};
building::building()
{
	settingroom = "客厅";
	bedroom = "卧室";
}

goodgay::goodgay()
{
	cout << &build << " " << build << endl;
	build = new building;
	cout << &build << " " << build << endl;
}

void goodgay::visit()
{
	cout << "客厅：" <<& build->settingroom << endl;
	cout << "卧室：" << build->bedroom << endl;
}
void goodgay::visit1()
{
	cout << "客厅：" << &build->settingroom << endl;
	//cout << "卧室：" << p->bedroom << endl;
}

void test01()
{
	goodgay gg;
	gg.visit();
	gg.visit1();
}
int main()
{
	test01();
    return 0;
}
