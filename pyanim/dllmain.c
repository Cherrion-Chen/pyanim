/* Replace "dll.h" with the name of your header */
#include "dll.h"
#include <windows.h>
#include <stdlib.h>
#include <math.h> 

BOOL WINAPI DLLMain(HINSTANCE hinstDLL,DWORD fdwReason,LPVOID lpvReserved)
{
	switch(fdwReason)
	{
		case DLL_PROCESS_ATTACH:
		{
			break;
		}
		case DLL_PROCESS_DETACH:
		{
			break;
		}
		case DLL_THREAD_ATTACH:
		{
			break;
		}
		case DLL_THREAD_DETACH:
		{
			break;
		}
	}
	return TRUE;
}

double *circle(double r, double x, double y){
	double *ls = (double *)calloc(512, 8);
	double s = 3.1415926/128, the = 0;
	for(int i=0; i<256; i++){
		*(ls+i) = x+r*cos(the);
		*(ls+256+i) = y+r*sin(the);
		the += s;
	}
	return ls;
}

double *ellipse(double a, double b){
	double *ls = (double *)calloc(512, 8);
	double s = 3.1415926/128, the = 0;
	for(int i=0; i<256; i++){
		*(ls+i) = a*cos(the);
		*(ls+256+i) = b*sin(the);
		the += s;
	}
	return ls;
}

double *parabola(double c, double min, double max){
	double *ls = (double *)calloc(512, 8);
	double s = (max-min)/256;
	for(int i=0; i<256; i++){
		*(ls+i) = min;
		*(ls+256+i) = pow(min, 2)/(4*c);
		min += s;
	}
	return ls;
}

double *hyperbola(double a, double b, double min, double max){
	double *ls = (double *)calloc(512, 8);
	double s = (max-min)/256;
	for(int i=0; i<256; i++){
		*(ls+i) = min;
		*(ls+256+i) = a*sqrt(1+pow(min, 2)/pow(b, 2));
		min += s;
	}
	return ls;
}
