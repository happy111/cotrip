import time, threading
from backgroundjobs.user_check import user_creation
from django.db import connections

WAIT_SECONDS = 3600
def update_userbase():
	user_basecheck = user_creation()
	print("Hi I am your autobot..you can call me Cerebro")
	print("At "+time.ctime()+" Cerebro starts its operation again!!")
	print("I will check and sync user base after every "+ str(WAIT_SECONDS) + " seconds!!")
	threading.Timer(WAIT_SECONDS, update_userbase).start()
	a = connections.close_all()

