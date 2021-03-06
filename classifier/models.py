from mongoengine import Document, EmbeddedDocument, fields


class ScoringData(Document):
    status_ml = fields.IntField(null=True) # credit status set by ml model
    status_ma = fields.IntField(null=True) #status set manually. superior than ml
    seniority = fields.IntField()
    home = fields.IntField()
    time = fields.IntField()
    age = fields.IntField()
    marital = fields.IntField()
    records = fields.IntField()
    job = fields.IntField()
    expenses = fields.IntField()
    income = fields.IntField()
    assets = fields.IntField()
    debt = fields.IntField()
    amount = fields.IntField()
    price = fields.IntField()
