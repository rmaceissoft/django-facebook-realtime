from django.dispatch import Signal

# triggered when a facebook realtime update is received
realtime_update = Signal(providing_args=["object_type",
                                         "uid",
                                         "changed_fields",
                                         "time",
                                         "request"])

