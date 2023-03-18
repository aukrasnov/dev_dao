## Week 6 Homework


Question  1:  Please select the statements that are correct
- Kafka Node is responsible to store topics (kafka broker)
- Zookeeper is removed form Kafka cluster starting from version 4.0 (no such version jet)
- **Retention configuration ensures the messages not get lost over specific period of time.**
- **Group-Id ensures the messages are distributed to associated consumers**


Question 2: Please select the Kafka concepts that support reliability and availability
- **Topic Replication** (if one broker fails, the data can still be accessed from another broker.)
- Topic Paritioning
- **Consumer Group Id**
- **Ack All** (Kafka allows producers to specify the number of acknowledgments they require before considering a message to be successfully sent)

Question 3: Please select the Kafka concepts that support scaling

- Topic Replication
- **Topic Partitioning** (Kafka partitions data across multiple brokers, which allows data to be distributed and processed in parallel.)
- **Consumer Group Id** (This enables horizontal scaling by allowing additional consumers to be added to the group as needed to handle increased load.)
- Ack All

Question 4: Please select the attributes that are good candidates for partitioning key. Consider cardinality of the field you have selected and scaling aspects of your application
- payment_type
- vendor_id
- passenger_count
- total_amount
- **tpep_pickup_datetime**
- **tpep_dropoff_datetime**


Question 5:  Which configurations below should be provided for Kafka Consumer but not needed for Kafka Producer

- Deserializer Configuration
- Topics Subscription
- Bootstrap Server
- **Group-Id**
- **Offset**
- Cluster Key and Cluster-Secret 