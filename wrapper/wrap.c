#include <Python.h>
PyObject* wrap_fact(PyObject* self, PyObject* args) 
{
  int n, result;
  
  if (! PyArg_ParseTuple(args, "i:fact", &n))
    return NULL;
  result = fact(n);
  return Py_BuildValue("i", result);
}
static PyMethodDef exampleMethods[] = 
{
  {"fact", wrap_fact, METH_VARARGS, "Caculate N!"},
  {NULL, NULL}
};
void initexample() 
{
  PyObject* m;
  m = Py_InitModule("example", exampleMethods);
}
