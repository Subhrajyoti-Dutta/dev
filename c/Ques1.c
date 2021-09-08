#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv) {
    //approximate values of 1/3: a) 0.3 b) 0.32 c) 0.33333
    double app[3] = { 0.3, 0.32, 0.33333 };
    double act_val = 1.0 / 3.0, app_val;
    double abs_err, rel_err, per_err;
    for (int i = 0; i < 3; i++) {
        app_val = app[i];
        printf("Approximate value: %lf\n", app_val);
        abs_err = fabs(act_val - app[i]);
        printf("\tAbsolute Error: %lf\n", abs_err);
        rel_err = abs_err / act_val;
        printf("\tRelative Error: %lf\n", rel_err);
        per_err = rel_err * 100;
        printf("\tPercentage Error: %lf\n\n", per_err);
    }
    return 0;
}