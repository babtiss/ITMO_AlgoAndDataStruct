#include <iostream>
#include <vector>

int main() {
    long long INF = 100000000000;
    long long n;
    std::cin >> n;

    std::vector<long long> d;
    long long a[n + 1];
    long long pos[n + 1];
    long long prev[n + 1];
    long long mx = -1;
    d.push_back(-INF);
    for (long long i = 0; i < n; i++) {
        pos[i] = -1;
        prev[i] = -1;
        std::cin >> a[i];
    }
    pos[n] = -1;

    for (long long i = 1; i <= n; i++)
        d.push_back(INF);

    long long right = 0;
    long long left = 0;
    for (long long i = 0; i < n; i++) {
        left = 0;
        right = n;
        while (right - left > 1) {
            long long middle = (left + right) / 2;
            if (d[middle] > a[i]) {
                right = middle;
            } else {
                left = middle;
            }
        }

        if ((d[right - 1] < a[i]) && (a[i] < d[right])) {
            d[right] = a[i];
            pos[right] = i;
            prev[i] = pos[right - 1];
            mx = std::max(mx, right);
        }

    }

    long long p = pos[mx];
    std::vector<long long> answer;

    while (p != -1) {
        answer.push_back(a[p]);
        p = prev[p];
    }
    std::cout << answer.size() << std::endl;
    for (long long i = answer.size() - 1; i >= 0; i--) {
        std::cout << answer[i] << ' ';

    }

}