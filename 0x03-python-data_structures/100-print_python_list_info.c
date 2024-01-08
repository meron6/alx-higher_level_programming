#include <Python.h>

int main(void)
{
    PyObject *list;
    PyObject *item1, *item2, *item3;

    Py_Initialize();

    item1 = PyUnicode_FromString("Hello");
    item2 = PyLong_FromLong(123);
    item3 = PyFloat_FromDouble(3.14);

    list = PyList_New(3);
    PyList_SetItem(list, 0, item1);
    PyList_SetItem(list, 1, item2);
    PyList_SetItem(list, 2, item3);

    print_python_list_info(list);

    Py_DECREF(list);
    Py_DECREF(item1);
    Py_DECREF(item2);
    Py_DECREF(item3);

    Py_Finalize();

    return (0);
}
