#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    long int size;
    char *data;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    data = PyBytes_AsString(p);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", data);

    printf("  first %li bytes:", (size < 10) ? size : 10);
    for (int i = 0; i < size && i < 10; i++)
        printf(" %02hhx", data[i]);
    printf("\n");
}
