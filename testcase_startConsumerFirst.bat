start cmd /C python .\consumer_hardware\hardwareConsumer.py

start cmd /C python .\consumer_software\softwareConsumer.py

timeout 3

cd .\producer\
python .\producercsv1.py

python .\producercsv2.py
cd..