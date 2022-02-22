#include <iostream>
#include <fstream>
using namespace std;


double* iter(double** a, double* y, int n)
{
	double* res = new double[n];
	int i, j;


	for (i = 0; i < n; i++)
	{
		res[i] = y[i] / a[i][i];
	}
	//точність визначення
	double eps = 0.0001;
	double* Xn = new double[n];
	//використання бескінечного цикла , так як виход із нього є в перевірці
	do {
		//цикл ітерації по елементам матриці
		for (i = 0; i < n; i++) {
			Xn[i] = y[i] / a[i][i];
			for (j = 0; j < n; j++) {
				if (i == j)
					continue;
				else {
					Xn[i] -= a[i][j] / a[i][i] * res[j];
				}
			}
		}
		//ітерація по елементам , якщо різниця по модулю наступного і минуулого більше за епсілон
		//тобто точність не дійшла до значення упсілон ,виходимо із циклу , так як наближення не є відпові..
		bool flag = true;
		for (i = 0; i < n - 1; i++) {
			if (abs(Xn[i] - res[i]) > eps) {
				flag = false;
				break;
			}
		}
		//збереження минулого значення  в res , щоб знову повернуись до першого циклу
		for (i = 0; i < n; i++) {
			res[i] = Xn[i];
		}
		// якщо цикл  == true ,цикл виконався без помилок, виход з циклу та повернення результату
		if (flag)
			break;
	} while (1);

	return res;
}

//Знаходження оберненої матриці
double** InvMatr(double** a, int n)
{
	double** res;
	double* y = new double[n];
	double* itr;
	int i, j, k;
	//виділення памяті для  збереження результату
	res = new double* [n];
	for (i = 0; i < n; i++)
	{
		res[i] = new double[n];
	}
	//цикл визначення оберненої матриці
	for (i = 0; i < n; i++)
		//заповнення і -стовбців
	{
		for (j = 0; j < n; j++)
			//цикл ,який заповнює одиничку матрицю 
		{
			//якщо і == j то це елемент головної діагоналі , то його заповнюєм одиицями
			if (i == j)
			{
				y[j] = 1;
			}
			//якшо ні то нулями, так як всі елементі за осн.діагоналю == 0 
			else
			{
				y[j] = 0;
			}
		}
		// функція з аргументами матриця/стовбець вільних значеь/розмірність
		itr = iter(a, y, n);
		//в  itr знаходиться обернений стовбець матриці
		for (k = 0; k < n; k++)
		{
			res[k][i] = itr[k];
		}
		//присвоюємо значення до результату
	}

	return res;
}



int main()
{
	setlocale(LC_ALL, "Russian");
	//оголошення 3 двомірних масивів
	double** a;
	double** x;
	double** c;
	//читання матриці з файлу 
	ifstream Infile;
	int n, i, j;
	cout << "Enter the dimension of the matrix: ";
	cin >> n;
	//відкритття текстового файлу
	Infile.open("inArray5.txt");
	//перевірка розмірності матриці
	if (n < 3)
	{
		 cout << "Error value degree 3" << endl;
		 exit;
	}
	//виділення памяті під матрицю
	a = new double* [n];
	for (i = 0; i < n; i++)
	{
		a[i] = new double[n];
	}
	//заповнення матриці із файлу
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			Infile >> a[i][j];
		}
	}
	//закриття файлу
	Infile.close();
	//виденння на екран матриці
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			cout << a[i][j] << "\t";
		}
		cout << endl;
	}
	cout << endl;
	//використання функції ImvMatr , де a - відповідна  матриця, n - розмірністть матриці 
	x = InvMatr(a, n);
	// вивід на  екран обернену матрицю 
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			cout << x[i][j] << "\t";
		}
		cout << endl;
	}
	cout << endl;

	
	return 0;
}

