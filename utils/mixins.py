class MultiSerializerMixin:
    serializer_action_map = {}

    def get_serializer_class(self):
        return self.serializer_action_map.get(
            self.action,
            self.serializer_class,
        )

    def get_default_serializer(self, *args, **kwargs):
        serializer_class = self.serializer_class
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)