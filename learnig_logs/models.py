from django.db import models

class Topic(models.Model):
    '''Um assunto sobre o qual o usuário está aprendendo'''
    text = models.CharField(max_length=200)
    date_added  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''devolve uma documentação em string do modelo'''
        return self.text

class Entry(models.Model):
    '''Algo especifico aprendido sobre um assunto'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'


    def __str__(self):
        #devolve uma string do modelo
        return self.text[:50] + '...'