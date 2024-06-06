import asyncio
from tinydb import TinyDB
import time
import threading
import random


class DB:
	_instances = {}  # Class-level dictionary to store instances
	_lock = threading.Lock()  # Class-level lock for thread-safe singleton creation

	def __new__(cls, path):
		with cls._lock:  # Ensure thread-safe singleton pattern
			if path not in cls._instances: cls._instances[path] = super(DB, cls).__new__(cls)
			return cls._instances[path]

	def __init__(self, path):
		if hasattr(self, 'is_initialized') and self.is_initialized: return

		self.path = path
		self.lock = threading.Lock()
		self.db = TinyDB(self.path)
		self.is_initialized = True  # Flag to prevent reinitialization

	def __enter__(self):
		self.lock.acquire()
		return self.db

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.lock.release()

# testing to see if the lock works with threads
# def test_lock(i):
# 	with DBWrapper('test.json') as db:
# 		db.insert({'test': 'test'})
# 		print("inserted", i)

# def main():
# 	threads = []
# 	for i in range(10):
# 		t = threading.Thread(target=test_lock, args=(i,))
# 		threads.append(t)
# 		t.start()

# 	for t in threads:
# 		t.join()

# if __name__ == '__main__':
# 	main()