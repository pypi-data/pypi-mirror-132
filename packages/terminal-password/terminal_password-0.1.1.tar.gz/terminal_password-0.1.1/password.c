#include <Python.h>
#include <stdlib.h>
#ifdef _WIN32
  #include <conio.h>
  #define ENCODING "GBK"
#else
  #include <termios.h>
  #define ENCODING "utf8"
#endif

#define PASSWORD_LENGTH 20

PyObject* test(PyObject* self, PyObject* args, PyObject*kw) {
	const char* key[] = {"char", NULL};
	PyObject *a = Py_BuildValue("s", "*");
	if (!PyArg_ParseTupleAndKeywords(args, kw, "|O", key, &a))
	{
		return NULL;
	}
    char* flag = PyBytes_AsString(PyUnicode_AsEncodedString(a,ENCODING,"ignore"));
	char *password = (char *) malloc(sizeof(char) * PASSWORD_LENGTH);
    #ifndef _WIN32
       struct termios its,newits;
       tcgetattr(fileno(stdin),&its);
	   newits = its;
	   newits.c_lflag &= ~(ICANON|ECHO);
       tcsetattr(fileno(stdin),TCSANOW,&newits);
    #endif
    printf("Password: ");
    int i;
    for (i = 0; i < PASSWORD_LENGTH; ++i) {
        #ifdef _WIN32
            int c = _getch();
        #else
            int c = getchar();
        #endif
        if (c == '\r'|| c=='\n') {
            password[i] = '\0';
            printf("\n");
            break;
        } else if (c == '\b') {
            if (i>0){
                printf("\b \b");
                if (strlen(flag)==2)
                {
                    printf("\b");
                }
                i = i - 2;
            } else{
                i = -1;
            }
        } else {
            password[i] = (char) c;
            printf("%s",flag);
        }
    }
    #ifndef _WIN32
        tcsetattr(fileno(stdin),TCSANOW,&its);
    #endif
    a = Py_BuildValue("s", password);
    free(password);
	return a;
}

static PyMethodDef passwordModuleMethods[] = {
	{"get_password",test, METH_VARARGS|METH_KEYWORDS,"get_password function"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef passwordModule = {
	PyModuleDef_HEAD_INIT,
	"password",
	"password Module",
	0,
	passwordModuleMethods
};

PyMODINIT_FUNC PyInit_terminal_password() {
	return PyModule_Create(&passwordModule);
}