import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='queue_name')

# Producer
def produce(data):
    # Publish data to the queue
    channel.basic_publish(exchange='', routing_key='queue_name', body=data)

# Consumer
def consume():
    # Consume data from the queue
    def callback(ch, method, properties, body):
        print(f'Received: {body}')

    channel.basic_consume(queue='queue_name', auto_ack=True, on_message_callback=callback)
    channel.start_consuming()

# Start the producer and consumer
produce('Hello, World!')
consume()

# Close the connection
connection.close()
