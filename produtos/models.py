from django.db import models
from stdimage.models import StdImageField

# Create your models here.

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data criação', auto_now_add=True)
    modificado = models.DateField('Data atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True


class Anuncio(Base):
    nome = models.CharField('Nome', max_length=150)
    preco = models.DecimalField('Preço', max_digits=15, decimal_places=2)
    contato = models.IntegerField('telefone')
    descricao = models.TextField('Descrição do Produto', blank=True)
    imagem = StdImageField('Imagem', upload_to='produto', blank=True, variations={'thumb': (124, 123)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)  
    
    def __str__(self):
        return self.nome
    
def anuncio_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(anuncio_pre_save, sender=Anuncio)