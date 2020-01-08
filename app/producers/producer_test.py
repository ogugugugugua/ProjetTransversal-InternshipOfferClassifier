import persistqueue
q = persistqueue.SQLiteQueue('queue', auto_commit=True)
q.put('un')
q.put('bon')
q.put('test')