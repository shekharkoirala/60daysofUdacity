import pika

# create a new instancce of the connection object
connection = pika.BlockingConnection(
	pika.ConnectionParameters(host='localhost'))

# Create a new channel with the next available channel number or pass in a channel number to use.
channel = connection.channel()

# Declare queue, create if needed. This method creates or checks a queue when created a new queue
channel.queue_declare(queue='hello4')

channel.basic_publish(exchange="", routing_key='hello4', body='Hello World!')

print("[x] sent Hello World!")

connection.close()
