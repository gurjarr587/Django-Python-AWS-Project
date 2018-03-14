
from __future__ import unicode_literals

from django.db import models

class admin_user(models.Model):
        admin_id = models.IntegerField(primary_key=True, db_column="admin_id")
        F_NAME = models.CharField(max_length=25, db_column="F_NAME")
        L_NAME = models.CharField(max_length=25, db_column="L_NAME")
        ADMIN_EMAIL_ID = models.TextField(max_length=25,db_column="ADMIN_EMAIL_ID")
        ADMIN_PASS = models.TextField(max_length=7,db_column="ADMIN_PASS")
        M_NAME = models.CharField(max_length=25, db_column="M_NAME")
        class Meta:
            db_table = 'admin_user'



class building_user(models.Model):
        B_ADMIN_ID = models.IntegerField(primary_key=True, db_column="B_ADMIN_ID")
        F_NAME = models.CharField(max_length=25, db_column="F_NAME")
        L_NAME = models.CharField(max_length=25, db_column="L_NAME")
        B_ADMIN_EMAIL_ID = models.TextField(max_length=25, db_column="B_ADMIN_EMAIL_ID")
        B_ADMIN_PASS = models.TextField(max_length=25, db_column="B_ADMIN_PASS")
        admin_id = models.ForeignKey(admin_user,db_column="admin_id")

        class Meta:
                db_table = 'building_user'


class normal_user(models.Model):
        USER_ID = models.IntegerField(primary_key=True, db_column="USER_ID")
        F_NAME = models.CharField(max_length=25, db_column="F_NAME")
        L_NAME = models.CharField(max_length=25, db_column="L_NAME")
        NORMAL_USER_EMAIL_ID = models.TextField(max_length=25, db_column="NORMAL_USER_EMAIL_ID")
        NORMAL_USER_PASS = models.TextField(max_length=25, db_column="NORMAL_USER_PASS")
        admin_id = models.ForeignKey(admin_user, db_column="admin_id")
        B_ADMIN_ID = models.ForeignKey(building_user, db_column="B_ADMIN_ID")

        class Meta:
                db_table = 'normal_user'


class department(models.Model):
        DEPT_ID = models.IntegerField(primary_key=True, db_column="DEPT_ID")
        DEPT_NAME = models.CharField(max_length=25, db_column="DEPT_NAME")
        admin_id = models.ForeignKey(admin_user,db_column="admin_id")
        B_ADMIN_ID = models.ForeignKey(building_user,db_column="B_ADMIN_ID")

        class Meta:
                db_table = 'department'


class message(models.Model):

        ENQUIRY = models.CharField(max_length=25, db_column="ENQUIRY")
        COMPLAINT = models.CharField(max_length=25, db_column="COMPLAINT")
        USER_ID = models.ForeignKey(normal_user)

        class Meta:
            db_table = 'message'



class room(models.Model):

        ROOM_ID = models.IntegerField(primary_key=25, db_column="ROOM_ID")
        ROOM_TYPE = models.TextField(max_length=25, db_column="ROOM_TYPE")
        USER_ID = models.ForeignKey(normal_user)
        B_ADMIN_ID = models.ForeignKey(building_user)

        class Meta:
            db_table = 'room'

class room_type(models.Model):
        ROOM_NAME = models.CharField(max_length=25, db_column="ROOM_NAME")
        CAPACITY = models.CharField(max_length=25, db_column="CAPACITY")
        ROOM_ID = models.ForeignKey(room)
        ROOM_STATUS = models.CharField(max_length=25, db_column="ROOM_STATUS")
        class Meta:
            db_table = 'room_type'
