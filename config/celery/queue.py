from kombu import Queue


class CeleryQueue:
    class Definitions:
        BEATS = "beats"
        EMAIL_NOTIFICATION = "email-notification"

    @staticmethod
    def queues():
        return tuple(
            (Queue(getattr(CeleryQueue.Definitions, item)))
            for item in filter(
                lambda ref: not ref.startswith("_"), dir(CeleryQueue.Definitions)
            )
        )
