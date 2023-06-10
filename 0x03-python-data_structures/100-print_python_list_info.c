#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    PyTypeObject *type;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        type = Py_TYPE(item);
        printf("Element %ld: %s\n", i, type->tp_name);
    }
}
