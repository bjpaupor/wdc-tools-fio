#include <math.h>
#include <assert.h>
#include <stdbool.h>
#include "lambertsw.h"

#define EPSILON 1e-09

/*
 * From https://www.quora.com/How-is-the-Lambert-W-Function-computed
 */

double lambertsw(const double x)
{
	double w, wnew, expw;

	wnew = x;

	do {
		w = wnew;
		expw = exp(w);

		wnew = w - (w * expw - x) / (w * expw + expw);
	} while (fabs(w - wnew) > EPSILON);

	return w;
}
