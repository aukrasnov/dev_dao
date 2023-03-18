package org.example;

import com.eclipsesource.json.Json;
import com.eclipsesource.json.JsonObject;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.example.data.FhvInfo;
import org.example.data.GreenFhv;
import org.example.data.GreenTrip;

import java.time.Duration;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalUnit;
import java.util.*;

import io.confluent.kafka.serializers.KafkaJsonDeserializerConfig;
public class JsonConsumer {

    private Properties props = new Properties();
    private KafkaConsumer<String, GreenFhv> consumer;
    public JsonConsumer() {
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "pkc-75m1o.europe-west3.gcp.confluent.cloud:9092");
        props.put("security.protocol", "SASL_SSL");
        props.put("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username='"+Secrets.KAFKA_CLUSTER_KEY+"' password='"+Secrets.KAFKA_CLUSTER_SECRET+"';");
        props.put("sasl.mechanism", "PLAIN");
        props.put("client.dns.lookup", "use_all_dns_ips");
        props.put("session.timeout.ms", "45000");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "io.confluent.kafka.serializers.KafkaJsonDeserializer");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "zoomcamp_group");
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        props.put(KafkaJsonDeserializerConfig.JSON_VALUE_TYPE, GreenFhv.class);
        consumer = new KafkaConsumer<String, GreenFhv>(props);
//        consumer.subscribe(List.of(Topics.INPUT_FHV_TOPIC, Topics.INPUT_GREEN_TOPIC));
        consumer.subscribe(Arrays.asList(Topics.INPUT_FHV_TOPIC, Topics.INPUT_GREEN_TOPIC));

    }

    public void consumeFromKafka() {
        System.out.println("Consuming form kafka started");
        var results = consumer.poll(Duration.of(10, ChronoUnit.SECONDS));
        Map<String, Integer> rideCounts = new HashMap<>();
        var i = 0;
        do {
//            System.out.println(String.valueOf(results.count()));
            for(ConsumerRecord<String, GreenFhv> ride: results) {
//                System.out.println(ride.value().DOLocationID);

                String locationID = String.valueOf(ride.value().PULocationID);
                if (rideCounts.containsKey(locationID)) {
                    int count = rideCounts.get(locationID);
                    rideCounts.put(locationID, count + 1);
                } else {
                    rideCounts.put(locationID, 1);
                }
            }
            System.out.println(rideCounts);
            i++;
        }
        while(!results.isEmpty() || i < 100);
    }

    public static void main(String[] args) {
        JsonConsumer jsonConsumer = new JsonConsumer();
        jsonConsumer.consumeFromKafka();
    }
}