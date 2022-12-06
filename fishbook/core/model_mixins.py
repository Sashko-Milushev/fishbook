
class StrFromFieldMixin:
    str_fields = ()

    def __str__(self):
        return ', '.join(
            f'{str_field}={getattr(self, str_field, None)}' for str_field in self.str_fields
        )


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())