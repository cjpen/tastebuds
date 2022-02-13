
class Event(models.Model):
    title = models.CharField(max_length=100)
    host = models.CharField(max_length=100) # potential to change to dropdown(Group Members)
    location = models.CharField(max_length=100)
    datetime = models.DateTimeField()

    group = models.ForeignKey(Group, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.group}'s event on {self.datetime}"

    
{% for event in group.event_set.all %}
<div class="card">
  <div class="card-content">
    <span class="card-title">{{ event.title }}</span>
    <p>Host: {{ event.host }}</p>
    <p>Location: {{ event.location }}</p>
    <p>Event Date: {{ event.datetime }}</p>
  </div>
</div>
{% endfor %}
