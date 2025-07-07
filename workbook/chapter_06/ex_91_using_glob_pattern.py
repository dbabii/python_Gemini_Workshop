import pathlib

p = pathlib.Path("")
# absolutely path
abs_p = pathlib.Path.cwd()

# find all *py files in current dir
py_files = p.glob("*.py")
print("*.py", list(py_files))
# find all *py files in current dir and sub-dirs
print("**/*.py", list(p.glob("**/*.py")))
# find all dirs in the current dir
print("*/*", list(p.glob("*/*")))
# provide a list with files only
print("Files in **/*", [f for f in p.glob("**/*py") if f.is_file()])
# All hidden
print("Hidden files:", list(p.glob('.*')))