from django.db import models

# Create your models here.
class CS2150(models.Model):
	letterGrade = models.CharField(max_length=5)
	grade = models.CharField(max_length=10)
	final_actual = models.CharField(max_length=5)
	final_max = models.CharField(max_length=5)
	exam_1_actual = models.CharField(max_length=5)
	exam_1_max = models.CharField(max_length=5)
	exam_2_actual = models.CharField(max_length=5)
	exam_2_max = models.CharField(max_length=5)
	pre_lab_1 = models.CharField(max_length=5)
	in_lab_1 = models.CharField(max_length=5)
	post_lab_1 = models.CharField(max_length=5)
	lab_1_max = models.CharField(max_length=5)
	pre_lab_2 = models.CharField(max_length=5)
	in_lab_2 = models.CharField(max_length=5)
	post_lab_2 = models.CharField(max_length=5)
	lab_2_max = models.CharField(max_length=5)
	pre_lab_3 = models.CharField(max_length=5)
	in_lab_3 = models.CharField(max_length=5)
	post_lab_3 = models.CharField(max_length=5)
	lab_3_max = models.CharField(max_length=5)
	pre_lab_4 = models.CharField(max_length=5)
	in_lab_4 = models.CharField(max_length=5)
	post_lab_4 = models.CharField(max_length=5)
	lab_4_max = models.CharField(max_length=5)
	pre_lab_5 = models.CharField(max_length=5)
	in_lab_5 = models.CharField(max_length=5)
	post_lab_5 = models.CharField(max_length=5)
	lab_5_max = models.CharField(max_length=5)
	pre_lab_6 = models.CharField(max_length=5)
	in_lab_6 = models.CharField(max_length=5)
	post_lab_6 = models.CharField(max_length=5)
	lab_6_max = models.CharField(max_length=5)
	pre_lab_7 = models.CharField(max_length=5)
	in_lab_7 = models.CharField(max_length=5)
	post_lab_7 = models.CharField(max_length=5)
	lab_7_max = models.CharField(max_length=5)
	pre_lab_8 = models.CharField(max_length=5)
	in_lab_8 = models.CharField(max_length=5)
	post_lab_8 = models.CharField(max_length=5)
	lab_8_max = models.CharField(max_length=5)
	pre_lab_9 = models.CharField(max_length=5)
	in_lab_9 = models.CharField(max_length=5)
	post_lab_9 = models.CharField(max_length=5)
	lab_9_max = models.CharField(max_length=5)
	pre_lab_10 = models.CharField(max_length=5)
	in_lab_10 = models.CharField(max_length=5)
	post_lab_10 = models.CharField(max_length=5)
	lab_10_max = models.CharField(max_length=5)
	pre_lab_11 = models.CharField(max_length=5)
	in_lab_11 = models.CharField(max_length=5)
	post_lab_11 = models.CharField(max_length=5)
	lab_11_max = models.CharField(max_length=5)
	pre_lab_12 = models.CharField(max_length=5)
	in_lab_12 = models.CharField(max_length=5)
	lab_12_max = models.CharField(max_length=5)

	def __str__(self):
		return self.grade