class BaseRepository:
    def __init__(self, model):
        self.model = model

    def find_by_id(self, record_id):
        return self.model.objects.filter(id=record_id).first()

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update(self, record_id, **kwargs):
        self.model.objects.filter(id=record_id).update(**kwargs)
        return self.find_by_id(record_id)

    def delete(self, record_id):
        record = self.find_by_id(record_id)
        if record:
            record.delete()
            return True
        return False

    def find_all(self, **filters):
        return self.model.objects.filter(**filters)
