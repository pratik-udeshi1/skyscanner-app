class ExcludeFieldsMixin:
    exclude_fields = ['created_at', 'updated_at', 'deleted_at', 'password']

    def get_fields(self):
        fields = super().get_fields()
        return {key: value for key, value in fields.items() if key not in self.exclude_fields}
