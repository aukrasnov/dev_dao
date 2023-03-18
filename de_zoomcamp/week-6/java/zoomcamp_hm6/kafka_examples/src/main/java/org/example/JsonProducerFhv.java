package org.example;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.streams.StreamsConfig;
import org.example.data.FhvInfo;
import org.example.data.GreenFhv;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.ExecutionException;
import java.util.stream.Stream;

public class JsonProducerFhv {
    private Properties props = new Properties();
    public JsonProducerFhv() {
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "pkc-75m1o.europe-west3.gcp.confluent.cloud:9092");
        props.put("security.protocol", "SASL_SSL");
        props.put("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username='"+Secrets.KAFKA_CLUSTER_KEY+"' password='"+Secrets.KAFKA_CLUSTER_SECRET+"';");
        props.put("sasl.mechanism", "PLAIN");
        props.put("client.dns.lookup", "use_all_dns_ips");
        props.put("session.timeout.ms", "45000");
        props.put(ProducerConfig.ACKS_CONFIG, "all");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, "io.confluent.kafka.serializers.KafkaJsonSerializer");
    }

    public Stream<FhvInfo> getRides() throws IOException, CsvException {
        var ridesStream = this.getClass().getResource("/fhv_tripdata_2019-01.csv");
        var reader = new CSVReader(new FileReader(ridesStream.getFile()));
        reader.skip(1);
        return reader.readAll().stream().map(FhvInfo::new);

    }

    public void publishRides(Stream<FhvInfo> rides) throws ExecutionException, InterruptedException {
        KafkaProducer<String, GreenFhv> kafkaProducer = new KafkaProducer<String, GreenFhv>(props);
        rides.forEach(ride -> {
            GreenFhv data = new GreenFhv(ride.PULocationID, ride.DOLocationID);
//            ride.tpep_pickup_datetime = LocalDateTime.now().minusMinutes(20);
//            ride.tpep_dropoff_datetime = LocalDateTime.now();
            var record = kafkaProducer.send(new ProducerRecord<>(Topics.INPUT_FHV_TOPIC, String.valueOf(ride.DOLocationID), data), (metadata, exception) -> {
                if(exception != null) {
                    System.out.println(exception.getMessage());
                }
            });
            try {
                System.out.println(record.get().offset());
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
            System.out.println(ride.DOLocationID);
//            Thread.sleep(500);
        });
    }



    public static void main(String[] args) throws IOException, CsvException, ExecutionException, InterruptedException {
        var producer = new JsonProducerFhv();
        var rides = producer.getRides();
        producer.publishRides(rides);
    }
}