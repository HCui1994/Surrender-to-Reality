#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char *argv[])
{
    int a[] = {5, 1, 12, 30, 20};
    std::vector<int> ivec(a, a + 5);
    for (std::vector<int>::iterator iter = ivec.begin(); iter != ivec.end(); iter++)
    {
        std::cout << *iter << " ";
    }
    std::cout << std::endl;

    std::make_heap(ivec.begin(), ivec.end());
    // ivec.pop_back();
    for (std::vector<int>::iterator iter = ivec.begin(); iter != ivec.end(); iter++)
    {
        std::cout << *iter << " ";
    }
    std::cout << std::endl;
}
