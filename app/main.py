import threading
import queue
import random
import time
import logging

from datetime import datetime

logging.basicConfig(level=logging.INFO)

class MultiThreadPractice():
    def __init__(self):
        self.share_q = queue.Queue(maxsize=10)

    def producer(self):
        while True:
            num = random.randint(1, 100)
            if not self.share_q.full():
                self.share_q.put(num)
                logging.info(f"Produced: {num}")
            else:
                logging.info('='*10)
                logging.info("Queue is full")
                logging.info('='*10)
            time.sleep(0.1)

    def consumer(self):
        while True:
            if not self.share_q.empty():
                num = self.share_q.get()
                logging.info(f"Consumed: {num}")
            else:
                logging.info('='*10)
                logging.info("Queue is empty")
                logging.info('='*10)

            time.sleep(0.15)

    def run_code(self):
        # Using daemon threading so the thread will be terminate after the timer.
        producer_thread = threading.Thread(target=self.producer, daemon=True)
        consumer_thread = threading.Thread(target=self.consumer, daemon=True)

        start_time = datetime.now()
        producer_thread.start()
        consumer_thread.start()

        time.sleep(10)
        end_time = datetime.now()
        logging.info(f'Totla run time will be {end_time - start_time}')

if __name__ == '__main__':
    mtp_app = MultiThreadPractice()
    mtp_app.run_code()