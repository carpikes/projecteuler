/* 2015-01-15 
 * compile with -std=c++11 -Wall -Werror
 */
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

const int tableWidth = 9;
const int tableHeight = 9;

void printSudoku(const int *sudoku) {
    for(int i=0;i<9;i++) {
        for(int j=0;j<9;j++)
            cout << sudoku[i*tableWidth + j] << " ";
        cout << endl;
    }
}

vector<int> getChoices(const int *sudoku, const int x, const int y) {
    vector<int> arr;
    int i, n;

    for(n=1;n<=9;n++) {
        for(i=0;i<9;i++) 
            if( sudoku[tableWidth * y + i] == n || // same row
                sudoku[tableWidth * i + x] == n || // same column
                sudoku[tableWidth * (i/3 + int(y/3)*3) + (i%3) + int(x/3) * 3] == n) // same cell
                break;
        
        if(i == 9)
            arr.push_back(n);
    } 

    return arr;
}

bool solveSudoku(int *sudoku, int x, int y) {
    if(y == tableHeight)
        return true;

    if(x == tableWidth)
        return solveSudoku(sudoku, 0, y + 1);

    if(sudoku[y * tableWidth + x] == 0) {
        vector<int> choices = getChoices(sudoku, x, y);

        for(auto i = choices.cbegin(); i != choices.cend(); ++i) {
            sudoku[y * tableWidth + x] = *i;
            if(solveSudoku(sudoku, x + 1, y))
                return true;
        }

        sudoku[y * tableWidth + x] = 0;
        return false;
    }
    
    return solveSudoku(sudoku, x+1, y);
}

int main() {
    ifstream in("in/96.txt"); 
    string line;
    int i,j, sudoku[tableWidth * tableHeight];

    int sum = 0;
    while(getline(in, line)) {
        for(i=0;i<tableHeight && getline(in, line);i++) {
            for(j=0;j<tableWidth;j++)
                if(line[j] >= '0' && line[j] <= '9')
                    sudoku[i*tableWidth+j] = line[j]-'0';
        }

        if(i == tableHeight && j == tableWidth) {
            if(!solveSudoku(sudoku,0,0))
                cerr << "Error" << endl;

            sum += sudoku[0] * 100 + sudoku[1] * 10 + sudoku[2]; 
        }
    }
    cout << sum << endl;
    return 0;
}
