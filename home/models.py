from django.db import models

# Create your models here.
class events(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="Uncategorized")
    description = models.CharField(max_length=400)
    detailed_description = models.TextField(default="")
    registration_Link = models.CharField(max_length=200)
    registration_LastDate = models.DateField()
    registration_fee = models.CharField(max_length=10, default="")
    eventImage = models.ImageField(upload_to='event_images/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    eventDate = models.DateField(blank=True, null=True)


class announcements(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    lastUpdate = models.DateField()




class timeLine(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    timeline_01 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_02 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_03 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_04 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_05 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_06 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_07 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_08 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_09 = models.CharField(max_length=100, default="",null=True, blank=True)
    timeline_10 = models.CharField(max_length=100, default="",null=True, blank=True)

class prizeMoney(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    first_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    second_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    third_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    fourth_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    fifth_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    sixth_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    seventh_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    eight_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    nineth_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    tenth_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    Eleventh_to_Twenty_prize = models.CharField(max_length=100, default="", null=True, blank=True)
    Twentyoneth_to_Fiftyth_prize = models.CharField(max_length=100, default="", null=True, blank=True)

    


class contactInfos(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)
    email = models.CharField(max_length=100)




class guidelines(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    guideline_Name = models.CharField(max_length=100)
    guideline_pdf = models.FileField(upload_to='guidelines/', blank=True, null=True)