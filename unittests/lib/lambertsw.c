#include <math.h>
#include "../unittest.h"

#include "../../lib/lambertsw.h"

/*
# ./LambertW1
W( -0.3679)=   -1.0000000000000000, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.3579)=   -1.2534937913672142, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.3479)=   -1.3726222651700963, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.3379)=   -1.4710267700264150, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.3279)=   -1.5594290674154530, check: exp(W(z))-z/W(z)=2.775558e-17
W( -0.3179)=   -1.6419951275144593, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.3079)=   -1.7208866490288997, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2979)=   -1.7974171543213702, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2879)=   -1.8724740958537323, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2779)=   -1.9467073111946138, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2679)=   -2.0206252287754034, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2579)=   -2.0946491590595939, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2479)=   -2.1691465881887817, check: exp(W(z))-z/W(z)=1.387779e-17
W( -0.2379)=   -2.2444532205670624, check: exp(W(z))-z/W(z)=1.387779e-17
W( -0.2279)=   -2.3208887515527370, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2179)=   -2.3987691379065947, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.2079)=   -2.4784170452512955, check: exp(W(z))-z/W(z)=-1.387779e-17
W( -0.1979)=   -2.5601716068913709, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.1879)=   -2.6443983736967955, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.1779)=   -2.7315002584038774, check: exp(W(z))-z/W(z)=1.387779e-17
W( -0.1679)=   -2.8219303365391082, check: exp(W(z))-z/W(z)=6.938894e-18
W( -0.1579)=   -2.9162075586046354, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.1479)=   -3.0149367879631335, check: exp(W(z))-z/W(z)=6.938894e-18
W( -0.1379)=   -3.1188351840000594, check: exp(W(z))-z/W(z)=-6.938894e-18
W( -0.1279)=   -3.2287679493980117, check: exp(W(z))-z/W(z)=6.938894e-18
W( -0.1179)=   -3.3457981311201119, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.1079)=   -3.4712580352563474, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.0979)=   -3.6068549325475114, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.0879)=   -3.7548332735187504, check: exp(W(z))-z/W(z)=3.469447e-18
W( -0.0779)=   -3.9182344244187823, check: exp(W(z))-z/W(z)=-3.469447e-18
W( -0.0679)=   -4.1013344732874799, check: exp(W(z))-z/W(z)=3.469447e-18
W( -0.0579)=   -4.3104309105895311, check: exp(W(z))-z/W(z)=1.734723e-18
W( -0.0479)=   -4.5553774654559378, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.0379)=   -4.8529292563991842, check: exp(W(z))-z/W(z)=3.469447e-18
W( -0.0279)=   -5.2352874987475646, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.0179)=   -5.7781951382155361, check: exp(W(z))-z/W(z)=-4.336809e-19
W( -0.0079)=   -6.7535694705172151, check: exp(W(z))-z/W(z)=-2.168404e-19
W(  -0.001)=   -9.1180064704027401, check: exp(W(z))-z/W(z)=0.000000e+00
W( -0.0001)=  -11.6671145325663552, check: exp(W(z))-z/W(z)=-6.776264e-21
W(  -1e-05)=  -14.1636008158101827, check: exp(W(z))-z/W(z)=1.058791e-22
W(  -1e-06)=  -16.6265089013724747, check: exp(W(z))-z/W(z)=-7.940934e-23
W(  -1e-07)=  -19.0660024220655480, check: exp(W(z))-z/W(z)=8.271806e-24
W(  -1e-08)=  -21.4881839440097977, check: exp(W(z))-z/W(z)=-6.203855e-25
W(  -1e-09)=  -23.8970195845316589, check: exp(W(z))-z/W(z)=-6.462349e-26
W(  -1e-10)=  -26.2952388192469257, check: exp(W(z))-z/W(z)=-1.615587e-27
W(  -1e-11)=  -28.6848035110810002, check: exp(W(z))-z/W(z)=-2.524355e-28
W(  -1e-12)=  -31.0671728420172322, check: exp(W(z))-z/W(z)=-4.417621e-29

 */

#define EPSILON 1e-08

static void test_lambertsw_1(void)
{
	int i;
	double z, w, check;

	/* from http://keithbriggs.info/software/LambertW.c */
	for (i = 0; i < 100; i++) {
		z = i/100.0 - 0.3678794411714423215955;
		w=lambertsw(z);
		check = exp(w) - z/w;
#ifdef LWDEBUG
		printf("W(%8.4f)=%22.16f, check: exp(W(z))-z/W(z)=%e\n", z, w, check);
#endif
		CU_ASSERT_FALSE(isnan(w));
		CU_ASSERT_TRUE(fabs(check) < EPSILON);
	}
}

static struct fio_unittest_entry tests[] = {
	{
		.name	= "lambertsw/1",
		.fn	= test_lambertsw_1,
	},
};

CU_ErrorCode fio_unittest_lib_lambertsw(void)
{
	return fio_unittest_add_suite("lib/lambertsw.c", NULL, NULL, tests);
}
