#include <iostream>
#include <algorithm>
#include <time.h>
#include <string>
#include <Windows.h>

using namespace std;

namespace Calculate {
	string Cutter(string num) {
		int i = 0;
		for (;num[i]!='1' && num[i]; i++) {
			continue;
		}
		
		string ret = num.substr(i);
		if (ret=="") ret = "0";
		return ret;
	}
	
	bool stringCMP(string num1, string num2) {
		if (num1.length()>num2.length()) return true;
		if (num1.length()<num2.length()) return false;
		return num1>num2;
	}
	
	string BasicAdd(bool node1, bool node2) {
		string first, second;
		string result= "";
        if (node1&&node2) first = "1";
		else first = "0";//!(node1&&node2)&&(node1||node2
		if (node1^node2) second = "1";
		else second = "0";
		result = first+second;
		return result;
	}
	
	string Addtion(string num1, string num2) {
		string ans = "";
		bool upper = false;
		int flen = num1.length(), slen = num2.length();
		int len = max(flen, slen);
		for (int i = 0; i<len; i++) {
			bool node1, node2;
			if (i<flen) {
				if (num1[i]=='0') node1 = false;
				else node1 = true;
			} else node1 = false;
			if (i<slen) {
				if (num2[i]=='0') node2 = false;
				else node2 = true;
			} else node2 = false;
			
			string str = BasicAdd(node1, node2);
			string strp = "";
			if (str[1]=='0') {
				strp = BasicAdd(0, upper);
			} else {
				strp = BasicAdd(1, upper);
			}
			
//			cout << str << " " << strp << upper << endl;
			
			if (str[0]=='1') upper = true;
			else if (strp[0]=='1') upper = true;
			else upper = false;

			ans = ans + strp[1];
		}
		if (upper) ans = ans+'1';
		return ans;
	}
	
	string Subtraction(string num1, string num2) {
		string ans = "";
		bool upper = false;
		int len = num1.length(), slen = num2.length();
//		cout << len <<  " " << num2 << endl;
		for (int i = 0; i<len; i++) {
			bool node1, node2;
			if (num1[i]=='0') node1 = false;
			else node1 = true;
			if (i<slen) {
				if (num2[i]=='0') node2 = true;
				else node2 = false;
			} else node2 = true;
			
//			cout << node1 << " " << node2 << endl;
			
			string str = BasicAdd(node1, node2);
			string strp = "";
			if (str[1]=='0') {
				strp = BasicAdd(0, upper);
			} else {
				strp = BasicAdd(1, upper);
			}
			
//			cout << str << " " << strp << upper << endl;
			
			if (str[0]!='0') upper = true;
			else if (strp[0]!='0') upper = true;
			else upper = false;

			ans = ans + strp[1];
		}
		string ans1 = Addtion(ans, "1");
		ans = "";
		for (int i = 0; i<len; i++) ans += ans1[i];
		return ans;
	}
	
	string Multiply(string num1, string num2) {
		if (num1.length()>num2.length()) swap(num1, num2);
		string ans = "0", plus="";
		for (int i = 0; i<num1.length(); i++) {
			if (num1[i]=='1') ans = Addtion(ans, plus+num2);
			plus += '0';
		}
		
		return ans;
	}
	
	pair <string, string> Division (string num1, string num2) {
		string quotient = "0", remain = "0";
		while (num1==num2 || stringCMP(num1, num2)) {
			string temp = num2, multi="1";
			
			while (stringCMP(num1, temp+"0")) {
				temp = temp+"0";
				multi = "0"+multi;
			}
			
			reverse(temp.begin(), temp.end());
			reverse(num1.begin(), num1.end());
			
			quotient = Addtion(quotient, multi);
			num1 = Subtraction(num1, temp);
			
			reverse(num1.begin(), num1.end());
			
			num1 = Cutter(num1);
		}
		
		return {quotient, num1};
	}
}

using namespace Calculate;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	bool sign = false;
	
	int nod1, nod2;	
	string node1, node2;
	
	cin >> node1 >> node2;
	
	pair <string, string> Div = Division(node1, node2);
	
	if (stringCMP(node2, node1)) {
		swap(node1, node2);
		sign = true;
	}
	
	reverse(node1.begin(), node1.end());
	reverse(node2.begin(), node2.end());
	
	string Add = Addtion(node1, node2), Sub = Subtraction(node1, node2), Mul = Multiply(node1, node2);
	int add=0, sub=0, mul=0;
	pair <int, int> div = {0, 0};
	
	reverse(Div.second.begin(), Div.second.end());
	
	for (int i = 0; Add[i]; i++) add += (Add[i]-'0')<<i;
	for (int i = 0; Sub[i]; i++) sub += (Sub[i]-'0')<<i;
	for (int i = 0; Mul[i]; i++) mul += (Mul[i]-'0')<<i;
	for (int i = 0; Div.first[i]; i++) div.first += (Div.first[i]-'0')<<i;
	for (int i = 0; Div.second[i]; i++) div.second += (Div.second[i]-'0')<<i;
	
	reverse(Add.begin(), Add.end());
	reverse(Mul.begin(), Mul.end());
	reverse(Sub.begin(), Sub.end());
	reverse(Div.first.begin(), Div.first.end());
	reverse(Div.second.begin(), Div.second.end());
	
	cout << add << endl;
	if (sign) cout << "-";
	cout << sub << endl;
	cout << mul << endl;
	cout << div.first << " " << div.second<<endl<<endl;
	
	cout << Add << endl;
	if (sign) cout << "-";
	cout << Sub << endl << Mul << endl << Div.first << " " << Div.second;
}
