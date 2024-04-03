#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    // Check if p is a valid PyListObject
    if (!PyList_Check(p)) {
        printf("[*] Python list information\n  [ERROR] Invalid List Object\n");
        return;
    }
    
    // Get the size of the list
    Py_ssize_t size = PyList_Size(p);
    
    // Get the list address in memory
    PyListObject *plist = (PyListObject *)p;
    void *list_address = (void *)p;
    
    // Print list information
    printf("[*] Python list information\n");
    printf("  [INFO] Size of the Python List = %ld\n", size);
    printf("  [INFO] Allocated = %ld\n", plist->allocated);
    printf("  [INFO] Address of the PyObject = %p\n", (void *)p);
    printf("  [INFO] Address of the PyListObject = %p\n", (void *)plist);
}

void print_python_bytes(PyObject *p) {
    // Check if p is a valid PyBytesObject
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }
    
    // Get the size of the bytes object
    Py_ssize_t size = PyBytes_Size(p);
    
    // Get the pointer to the bytes data
    char *bytes_data = PyBytes_AsString(p);
    
    // Print bytes information
    printf("[.] bytes object info\n");
    printf("  [INFO] Size: %ld\n", size);
    printf("  [INFO] trying string: %s\n", bytes_data);
    printf("  [INFO] Address of the PyObject: %p\n", (void *)p);
}

void print_python_float(PyObject *p) {
    // Check if p is a valid PyFloatObject
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }
    
    // Get the floating point value
    double value = PyFloat_AsDouble(p);
    
    // Print float information
    printf("[.] float object info\n");
    printf("  [INFO] value: %f\n", value);
}

