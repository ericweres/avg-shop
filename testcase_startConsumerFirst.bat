start cmd /C python .\consumer_hardware\hardwareConsumer.py

start cmd /C python .\consumer_software\softwareConsumer.py

timeout 10

cd .\producer\

start cmd /C python .\producercsv1.py

start cmd /C python .\producercsv2.py

cd ..