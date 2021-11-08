#include <iostream>

#include <fstream>

#include <string>

using namespace std;

​

int main()

{

ifstream is{ "C:\\WINDOWS\\system.ini" };

if (is.fail())

{

cout << "Cannot open is file." << endl;

exit(1);

}

while (!is.eof())

{

string str;

string find_str = "FON";

getline(is, str);

str.replace(str.find(find_str), 3, "DAT");

cout << str << endl;

}

​

is.close();

}