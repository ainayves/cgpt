from threading import Thread

global thread_store
thread_store = []

def insert_thread(t : Thread):

    thread_store.append(t)

