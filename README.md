# AVG Gruppe 6 | MOM Sim

+ Die Anwendung ist auf mehrere verschiedene "Projekte" aufgebaut
    + Ein Consumer, der Hardware-Aufträge konsumiert.
    + Ein Consumer, der Software-Aufträge konsumiert.
    + Ein bzw. mehrere Producer, die den Auftrag abschicken.
+ Das Ausführen des RabbitMQ-Servers ist mit Docker zu gewährleisten.
+ Test Cases sind mit automatisierten Batch-Skripten gestellt.

## How to Run

1. Rabbit Server starten (in root-dir):
   
      ```shell
      docker compose up
      ```
2. Ausführen der jeweiligen Services(Consumer oder Producer in einer shell)

3. Alternativ die **testcases** durchspielen.   

4. Rabbit server runterfahren:
    ```shell
    docker compse down
    ```
