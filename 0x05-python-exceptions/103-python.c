#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("Error: Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the list = %zd\n", size);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *itemType = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, itemType);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("Error: Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] Bytes object info\n");
    printf("  Size: %zd\n", size);
    printf("  Trying string: %s\n", PyBytes_AsString(p));

    if (size > 10)
        size = 10;

    printf("  First %zd bytes: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}


void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("Error: Invalid PyFloatObject\n");
        return;
    }

    printf("[.] Float object info\n");
    printf("  Value: %f\n", PyFloat_AS_DOUBLE(p));
}
