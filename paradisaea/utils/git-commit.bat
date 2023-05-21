set arg1=%1
set arg2=%2
powershell -Command "cd %arg2%;ls; git add .; git commit -m '%arg1%'"