//2.类做友元
class building
{
	friend class goodgay;
public:
	building()
	{
		this->settingroom = "客厅";
		this->bedroom = "卧室";
	}
public:
	string settingroom = "客厅";
    string settingroom;
	string chicken = "beaf";
private:
	string bedroom;
};

class goodgay
{
public:
	void visit()
	{
		cout << build->settingroom <<"地址："<<(int)&build->settingroom << endl;
		cout << build->bedroom << endl;
	 }
	goodgay()
	{
		build = new building;//创造建筑物对象???????????????
	}//new申请类空间时会自动调用构造函数
	building * build;
};


void test01()
{
	goodgay gg;
	gg.visit();
	
}

int main()
{
	building* b = new building();
	cout<<b->chicken<<"  "<< & b->chicken << endl;
	b->settingroom = "keting";
	cout << b->settingroom <<(int)&b->settingroom << endl;
	building c;
	cout << c.settingroom << (int)&c.settingroom << endl;
	test01();
	return 0;
}
