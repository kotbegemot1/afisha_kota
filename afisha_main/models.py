from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField("Заголовок",max_length=50)
    description = models.TextField("Описание")
    place = models.ForeignKey("Place", verbose_name="Место проведения", on_delete=models.PROTECT)
    event_date = models.DateTimeField("Время проведения", auto_now=False, auto_now_add=False)
    category = models.CharField("Категория", max_length=50)
    time_create = models.DateTimeField("Время создания", auto_now=False, auto_now_add=True)
    time_update = models.DateTimeField("Время обновления", auto_now=True, auto_now_add=False)
    genre = models.CharField("Жанр", max_length=50)
    # artist = models.ManyToManyField("app.Model", verbose_name=_(""))
    # poster = models.ImageField(_("Постер"), upload_to=None, height_field=None, width_field=None, max_length=None)
    # organizer = models.ManyToManyField("app.Model", verbose_name=_(""))

    def __str__(self):
        return self.title
    

class Place(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    address = models.CharField("Адрес", max_length=50)
    # type_building = models.CharField(_(""), max_length=50)

    def __str__(self):
        return self.name
    