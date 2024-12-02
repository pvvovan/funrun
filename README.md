## Execution time trace chart

Create project:
cmake -S ./ --preset Debug

Build project:
cmake --build --preset Debug --parallel

Clean project:
cmake --build --preset Debug --target 'clean'

Run on https://github.com/pvvovan/rustyh7/tree/main/pcb723
stty -F /dev/ttyACM0 115200 cs8 -cstopb -parenb
cat /dev/ttyACM0 > ./funtrace.json

Load funtrace.json in performance of web browser developer tools
