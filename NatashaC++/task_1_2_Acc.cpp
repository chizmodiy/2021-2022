#include <iostream>
#include <ctime>
#include <cmath>
#include <fstream>





using namespace std;
ifstream Infile;
template <typename T> void FreeMem(T** matr, int n);
template <typename T> void PrintMtx(T** matr, int n);
template <typename T> void SetMtx(T** matr, int n);
template <typename T> void TransponMtx(T** matr, T** tMatr, int n);
void Get_matr(int** matr, int n, int** temp_matr, int indRow, int indCol);
int matrixDet(int** matrix, int size);
void getMatrixWithoutRowAndCol(int** matrix, int size, int row, int col, int** newMatrix);
int Det(int** matr, int n);








void main()
{
    //розмір матриці та перевірка умови n < 3
    setlocale(0, "");
    int n, det;
    cout << "Введите размер матрицы: ";
    cin >> n;
    if (n < 3) {
        cout << "Введите значение больше 3" << endl;
        exit;
    }
    //виділення памяті для матриці, оберненої матриці, транспортованої матриці. 
    int** matr = new int* [n];
    double** obr_matr = new double* [n];
    double** tobr_matr = new double* [n];
    
    for (int i = 0; i < n; i++) {
        matr[i] = new int[n];
        obr_matr[i] = new double[n];
        tobr_matr[i] = new double[n];
    }
    //заповнення та друк матриці з текстового файлу  TEXT.txt.
    SetMtx(matr, n);
    PrintMtx(matr, n);
    //збереження значення визначника в змінну det.
    det = matrixDet(matr, n);
    cout << "Определитель матрицы = " << det << endl;
    if (det) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int m = n - 1;
                int** temp_matr = new int* [m];
                for (int k = 0; k < m; k++)
                    temp_matr[k] = new int[m];
                getMatrixWithoutRowAndCol(matr,n,i,j , temp_matr);
                obr_matr[i][j] = pow(-1.0, i + j + 2) * matrixDet(temp_matr, m) / det;
                FreeMem(temp_matr, m);
            }
        }
    }
    else
        cout << "Т.к. определитель матрицы = 0,\nто матрица обратной не имеет!" << endl;
    //Транспонування матриці.
    TransponMtx(obr_matr, tobr_matr, n);
    //Друк оберненої матриці після транспонування
    PrintMtx(tobr_matr, n);
    FreeMem(tobr_matr, n);
    FreeMem(matr, n);
    FreeMem(obr_matr, n);
}






//Функція транспонування матриці
template <typename T> void TransponMtx(T** matr, T** tMatr, int n) {//
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            tMatr[j][i] = matr[i][j];
}
//Функція звільнення памяті
template <typename T> void FreeMem(T** matr, int n)
{
    for (int i = 0; i < n; i++)
        delete[] matr[i];
    delete[] matr;
}

//функція заповнення матриці
template <typename T> void SetMtx(T** matr, int n)
{
    Infile.open("TEXT.txt");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            Infile >> matr[i][j];
}

//функція друку матриці
template <typename T> void PrintMtx(T** matr, int n)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cout << matr[i][j] << "  ";
        cout << endl;
    }
}

void Get_matr(int** matr, int n, int** temp_matr, int indRow, int indCol)
{
    int ki = 0;
    for (int i = 0; i < n; i++) {
        if (i != indRow) {
            for (int j = 0, kj = 0; j < n; j++) {
                if (j != indCol) {
                    temp_matr[ki][kj] = matr[i][j];
                    kj++;
                }
            }
            ki++;
        }
    }
}
// функція викреслення рядка та стовпця
void getMatrixWithoutRowAndCol(int** matrix, int size, int row, int col, int** newMatrix) {
    int offsetRow = 0;
    int offsetCol = 0;
    for (int i = 0; i < size - 1; i++) {
        if (i == row) {
            offsetRow = 1;
        }

        offsetCol = 0;
        for (int j = 0; j < size - 1; j++) {
            if (j == col) {
                offsetCol = 1;
            }

            newMatrix[i][j] = matrix[i + offsetRow][j + offsetCol];
        }
    }
}

//визначення визначника матриці

int matrixDet(int **matrix, int size) {
  int det = 0;
  int degree = 1; 
 
  if(size == 1) {
    return matrix[0][0];
  }
  if(size == 2) {
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0];
  }
 
  int **newMatrix = new int*[size-1];
  for(int i = 0; i < size-1; i++) {
    newMatrix[i] = new int[size-1];
  }
  for(int j = 0; j < size; j++) {
    getMatrixWithoutRowAndCol(matrix, size, 0, j, newMatrix);
    det = det + (degree * matrix[0][j] * matrixDet(newMatrix, size-1));
    degree = -degree;
  }
  for(int i = 0; i < size-1; i++) {
    delete [] newMatrix[i];
  }
  delete [] newMatrix;
 
  return det;
}
