#include "Python.h"


#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("[ERROR] Invalid string object\n");
        return;
    }

    PyObject *encoded_str = PyUnicode_AsUTF8String(p);
    if (encoded_str == NULL) {
        printf("[ERROR] Failed to encode string\n");
        return;
    }

    const char *str = PyBytes_AsString(encoded_str);
    if (str == NULL) {
        printf("[ERROR] Failed to decode string\n");
        Py_DECREF(encoded_str);
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);

    printf("String: %.*s\n", (int)length, str);
    printf("Length: %ld\n", length);

    Py_DECREF(encoded_str);
}
