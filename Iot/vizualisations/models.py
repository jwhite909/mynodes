from django.db import models

class Vizualisation(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        
class Node(models.Model):
    ip = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.ip
    


class Edge(models.Model):
    vizualisation = models.ForeignKey(Vizualisation, on_delete=models.CASCADE)
    src = models.ForeignKey(Node, related_name="source", on_delete=models.CASCADE)
    dest = models.ForeignKey(Node, related_name="destination", on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    volume = models.IntegerField(default=0)



