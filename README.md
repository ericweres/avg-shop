# AVG Gruppe 6 | MOM Sim

+ Die Anwendung ist auf mehrere verschiedene "Projekte" aufgebaut
    + Ein Consumer, der Hardware-Aufträge konsumiert.
    + Ein Consumer, der Software-Aufträge konsumiert.
    + Mehrere Producer, die den Auftrag abschicken.
+ Das Ausführen des RabbitMQ-Servers ist mit Docker zu gewährleisten.
+ Test Cases sind mit automatisierten Batch-Skripten gestellt.

## How to Run

1. Rabbit Server starten (in root-dir):
      ```shell
      docker compose up
      ```
2. Ausführen der jeweiligen Services(Consumer oder Producer in einer shell)
      ```shell
      cd producer
		python .\producercsv1.py
		python .\producercsv2.py
      ```
	  ```shell
      cd consumer_hardware
		python .\hardwareConsumer.py
      ```
	  ```shell
      cd consumer_software
		python .\softwareConsumer.py
      ```

3. **Alternativ** die Testcases durchspielen (in root-dir).

     Consumer ist gestartet und Producer wird später gestartet:
	```shell
    .\testcase_startConsumerFirst.bat
    ```
	 Producer ist gestartet und Consumer wird später gestartet:
	```shell
    .\testcase_startProducerFirst.bat
    ```

4. Rabbit server runterfahren:
    ```shell
    docker compse down
    ```
