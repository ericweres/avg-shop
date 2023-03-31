cd .\producer\
python .\producercsv1.py

python .\producercsv2.py
cd..

timeout 3

start cmd /C python .\consumer_hardware\hardwareConsumer.py

start cmd /C python .\consumer_software\softwareConsumer.py