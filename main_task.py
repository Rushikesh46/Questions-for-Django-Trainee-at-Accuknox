# Topic: Django Signals

# Question 1: By default are Django signals executed synchronously or asynchronously?
# Answer: Django signals are executed synchronously by default. This means that when an event occurs, the signal is sent, and its handler is executed immediately. The main process will wait for the signal handler to complete before moving on to the next operation.

      import time
      from myapp.models import MyModel

      def my_signal_handler(sender, instance, **kwargs):
          print("Signal handler started")
          time.sleep(5)  # Simulates a delay
          print("Signal handler finished")
      
      my_instance = MyModel.objects.create(field="value")
      print("Model saved")

# ___________________________________________________________________________

# Question 2: Do Django signals run in the same thread as the caller?
# Answer: Yes, by default, Django signals run in the same thread as the caller.Both the main function and the signal handler execute in the same thread.

      import threading
      
      def my_signal_handler(sender, instance, **kwargs):
          print(f"Signal handler thread: {threading.current_thread().name}")
      
      print(f"Main thread: {threading.current_thread().name}")
      my_instance = MyModel.objects.create(field="value")

# ___________________________________________________________________________

# Question 3: By default do Django signals run in the same database transaction as the caller?
# Answer: Yes, Django signals are part of the same database transaction by default. If an error occurs inside a signal handler, it can roll back the entire transaction.

      from django.db import transaction
      
      def my_signal_handler(sender, instance, **kwargs):
          print("Signal handler started")
          if instance.field == 'rollback':
              raise Exception("Triggering rollback")
          print("Signal handler finished")
      
      try:
          with transaction.atomic():
              my_instance = MyModel.objects.create(field='rollback')
              print("Model saved")
      except Exception as e:
          print(f"Transaction rolled back: {e}")

# ___________________________________________________________________________

# Topic: Custom Classes in Python

# Task: Create a Rectangle clas

      class Rectangle:
          def __init__(self, length: int, width: int):
              self.length = length
              self.width = width
      
          def __iter__(self):
              yield {'length': self.length}
              yield {'width': self.width}
      
      rect = Rectangle(10, 5)
      for dimension in rect:
          print(dimension)
