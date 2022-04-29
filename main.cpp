#include <iostream>
#include "poly34.h"

int main(int argc, char const *argv[])
{
    double a = 0.3801,
        b = -1.2969,
        c = -0.559,
        d = 1.0286
    ;

    double sol[3];

    int numsols = SolveP3(sol, b/a, c/a, d/a);

    double treal = 1e7f;
    if(numsols==1) {
        treal = sol[0];
    }
    else {
        for (int i = 0; i < numsols; ++i)
        {
            if (sol[i] > 0 )
                treal = std::min(treal, sol[i]);
        }
    }

    std::cout << "found sol: " << treal << std::endl;

    return 0;
}