import pika

# create a new instancce of the connection object
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
# Create a new channel with the next available channel number or pass in a channel number to use.
channel = connection.channel()
# Declare queue, create if needed. This method creates or checks a queue when created a new queue
channel.queue_declare(queue='hello4')
def callback(ch, method, properties, body):
    print(" [X[ received %r" % body)

channel.basic_consume(on_message_callback=callback, queue="hello4", auto_ack=True)

print(' [x] waiting for message . TO exit press ctrl + c')

channel.start_consuming()
