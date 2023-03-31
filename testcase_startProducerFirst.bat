cd .\producer\

start cmd /C python .\producercsv1.py

start cmd /C python .\producercsv2.py

cd ..

timeout 3

start cmd /C python .\consumer_hardware\hardwareConsumer.py

start cmd /C python .\consumer_software\softwareConsumer.py