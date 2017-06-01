from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
 first_name = models.CharField(max_length=255)
 last_name = models.CharField(max_length=255)
 email = models.CharField(max_length=255)
 password = models.CharField(max_length=255)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

 def __unicode__(self):
   return "id: " + str(self.id) + ", first_name: " + self.first_name + ", last_name: " + self.last_name + ", email" + self.email + ", password: " + self.password

class Message(models.Model):
 message = models.TextField(max_length=1000)
 user = models.ForeignKey(User, related_name="users1")
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 
 def __unicode__(self):
 	return "id: " + str(self.id) + ", message: " + self.message + ", user_id: " + str(self.user.id) + ", user_first_name: " + self.user.first_name + ", user_last_name: " + self.user.last_name + ", email: " + self.user.email + ", password: " + self.user.password

class Comment(models.Model):
 comment = models.TextField(max_length=1000)
 message = models.ForeignKey(Message, related_name="messages")
 user = models.ForeignKey(User, related_name="users2")
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

 def __unicode__(self):
 	return	"id: " + str(self.id) + ", comment: " + self.comment + ", message_id: " + str(self.message.id) + ", message_message: " + self.message.message + ", user_id: " + str(self.user_id) + ", user_first_name: " + self.user.first_name + ", user_last_name: " + self.user.last_name + ", email: " + self.user.email + ", password: " + self.user.password 

# class Dojo(models.Model):
#  location = models.CharField(max_length=38) #ex: San Jose, Seattle
#  state = models.CharField(max_length=38) #ex: CA, WA
#  created_at = models.DateTimeField(auto_now_add=True)
#  updated_at = models.DateTimeField(auto_now=True)

#  def __unicode__(self):
#    return "id: " + str(self.id) + ", location: " + self.location + ", state: " + self.state


# class Instructor(models.Model):
#  first_name = models.CharField(max_length=38)
#  created_at = models.DateTimeField(auto_now_add=True)
#  updated_at = models.DateTimeField(auto_now=True)
#  dojo = models.ForeignKey(Dojo, related_name="instructors")

#  def __unicode__(self):
#    return "id: " + str(self.id) + ", first_name: " + self.first_name + ", dojo_id: " + str(self.dojo.id) + "dojo_location: " + self.dojo.location

# class DryEraseMarker(models.Model):
#  color = models.CharField(max_length=38)
#  instructor = models.ForeignKey(Instructor, related_name="drymarker")
#  created_at = models.DateTimeField(auto_now_add=True)
#  updated_at = models.DateTimeField(auto_now=True)

#  def __unicode__(self):
#  	return self.color








