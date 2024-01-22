#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i)
    {
        printf("%02hhx ", string[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
