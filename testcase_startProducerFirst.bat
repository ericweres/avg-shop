cd producer
python .\producercsv.py

timeout 3

cd..
start cmd /C python .\receiver_hardware\rechw.py

start cmd /C python .\receiver_software\recsw.py