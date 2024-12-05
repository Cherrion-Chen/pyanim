#ifndef _DLL_H_
#define _DLL_H_

#if BUILDING_DLL
#define DLLIMPORT __declspec(dllexport)
#else
#define DLLIMPORT __declspec(dllimport)
#endif

DLLIMPORT double *circle(double r, double x, double y);
DLLIMPORT double *ellipse(double a, double b);
DLLIMPORT double *parabola(double c, double min, double max);
DLLIMPORT double *hyperbola(double a, double b, double min, double max);
DLLIMPORT void free_mem(double *l);

#endif