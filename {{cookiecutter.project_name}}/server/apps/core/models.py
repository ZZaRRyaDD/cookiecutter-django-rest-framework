from django.core.exceptions import ValidationError
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """Base model for apps' models.

    This class adds to models created and modified fields

    """

    def clean(self):
        """Validate model data.

        First we collect all errors as dict and then if there any errors, we
        pass them ValidationError and raise it. By doing this django admin and
        drf can specify for each field an error.

        """
        super().clean()
        errors = {}
        for field in self._meta.fields:
            clean_method = f"clean_{field.name}"
            if hasattr(self, clean_method):
                try:
                    getattr(self, clean_method)()
                except ValidationError as error:
                    errors[field.name] = error
        if errors:
            raise ValidationError(errors)

    def save(self, **kwargs):
        """Overriden for get update fields when object update."""
        if self.pk:
            cls = self.__class__
            old = cls.objects.get(pk=self.pk)
            changed_fields = []
            for field in cls._meta.get_fields():
                if hasattr(old, field.name) and hasattr(self, field.name):
                    if getattr(old, field.name) != getattr(self, field.name):
                        changed_fields.append(field.name)
            kwargs["update_fields"] = changed_fields
        super().save(**kwargs)

    class Meta:
        abstract = True
