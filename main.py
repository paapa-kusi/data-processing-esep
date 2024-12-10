class InMemoryDB:
    def __init__(self):
        self.db = {}
        self.transaction = None

    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("Transaction already in progress")
        self.transaction = {}

    def put(self, key, value):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.transaction[key] = value
    def get(self, key):
        if self.transaction is not None and key in self.transaction:
            return None
        return self.db.get(key, None)
    def commit(self):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.db.update(self.transaction)
        self.transaction = None
    def rollback(self):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.transaction = None


db = InMemoryDB()

print(db.get("A"))
try:
    db.put("A", 5)
except Exception as e:
    print(e)

db.begin_transaction()
db.put("A", 5)
print(db.get("A"))
db.put("A", 6)
db.commit()
print(db.get("A"))

try:
    db.commit()
except Exception as e:
    print(e)

db.begin_transaction()
db.put("B", 10)
db.rollback()
print(db.get("B"))
