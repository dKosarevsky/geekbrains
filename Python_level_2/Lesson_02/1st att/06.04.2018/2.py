
class CSomething:

    def to_json(self):

        return a # a - str

    @staticmethod
    def from_json(a):

        return CSomething()

# mongo
# pymongo
# collection.find() - ObjectId
# aggregate

obj = CSomething()

obj.to_json()
CSomething.to_json(obj)

CSomething.from_json("adadasd")

