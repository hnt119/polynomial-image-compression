#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    constexpr int q = 13;
    constexpr int ALL = (1 << q) - 1;
    // qval[x][y] = x^2 + xy + y^2 mod 13.
    int qval[q][q];
    for (int x = 0; x < q; ++x)
        for (int y = 0; y < q; ++y)
            qval[x][y] = (x*x + x*y + y*y) % q;

    int global_slack = 1000000;
    int global_T = 0, global_edges = 0;
    std::array<int, q + 1> best_edges_by_m{};
    std::array<int, q + 1> best_T_by_m{};

    std::vector<uint16_t> inter(1 << q);
    std::vector<int16_t> dp(1 << q);

    for (int T = 0; T <= ALL; ++T) {
        int m = __builtin_popcount((unsigned)T);
        uint16_t rows_for_col[q];
        for (int y = 0; y < q; ++y) {
            int rows = 0;
            for (int x = 0; x < q; ++x)
                if (T & (1 << qval[x][y])) rows |= (1 << x);
            rows_for_col[y] = rows;
        }

        inter[0] = ALL;
        dp[0] = 0;
        for (int S = 1; S <= ALL; ++S) {
            int bit = S & -S;
            int y = __builtin_ctz((unsigned)bit);
            inter[S] = inter[S ^ bit] & rows_for_col[y];
            int best_prev = -30000;
            int U = S;
            while (U) {
                int b = U & -U;
                best_prev = std::max<int>(best_prev, dp[S ^ b]);
                U ^= b;
            }
            dp[S] = best_prev + __builtin_popcount((unsigned)inter[S]);
        }

        int e = dp[ALL];
        if (e > best_edges_by_m[m]) {
            best_edges_by_m[m] = e;
            best_T_by_m[m] = T;
        }
        int slack = q*m - e;
        if (slack < global_slack) {
            global_slack = slack;
            global_T = T;
            global_edges = e;
        }
    }

    std::cout << "m best_edges slack T_values\n";
    for (int m = 0; m <= q; ++m) {
        std::cout << m << ' ' << best_edges_by_m[m] << ' '
                  << q*m - best_edges_by_m[m] << " {";
        bool first = true;
        int T = best_T_by_m[m];
        for (int t = 0; t < q; ++t) if (T & (1 << t)) {
            if (!first) std::cout << ',';
            first = false;
            std::cout << t;
        }
        std::cout << "}\n";
    }
    std::cout << "global slack " << global_slack << " edges "
              << global_edges << " Tmask " << global_T << "\n";
}
