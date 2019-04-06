from django.shortcuts import redirect, render
from django.template import Template, Context
from gradebook.models import *
from gradebook.forms import *

# Create your views here.
def cs2150(request):
	template = "cs2150.html"
	form = cs2150Gradebook(request.POST or None,
		initial = {'lab_1_max': '30', 'lab_2_max': '30', 'lab_3_max': '30', 'lab_4_max': '30', 'lab_5_max': '30', 'lab_6_max': '30',
					'lab_7_max': '30', 'lab_8_max': '30', 'lab_9_max': '30', 'lab_10_max': '30', 'lab_11_max': '30', 'lab_12_max': '20',}
					# 'final_actual' : '77', 'final_max' : '100', 'exam_1_actual' : '41', 'exam_1_max' : '70', 'exam_2_actual' : '36', 'exam_2_max' : '45',
					# 'pre_lab_1' : '10', 'in_lab_1' : '10', 'post_lab_1' : '10', 'pre_lab_2' : '10', 'in_lab_2' : '10', 'post_lab_2' : '10',
					# 'pre_lab_3' : '10', 'in_lab_3' : '10', 'post_lab_3' : '10', 'pre_lab_4' : '10', 'in_lab_4' : '10', 'post_lab_4' : '10',
					# 'pre_lab_5' : '10', 'in_lab_5' : '10', 'post_lab_5' : '10', 'pre_lab_6' : '10', 'in_lab_6' : '10', 'post_lab_6' : '10',
					# 'pre_lab_7' : '10', 'in_lab_7' : '10', 'post_lab_7' : '10', 'pre_lab_8' : '10', 'in_lab_8' : '10', 'post_lab_8' : '10',
					# 'pre_lab_9' : '10', 'in_lab_9' : '10', 'post_lab_9' : '10', 'pre_lab_10' : '10', 'in_lab_10' : '10', 'post_lab_10' : '10',
					# 'pre_lab_11' : '10', 'in_lab_11' : '10', 'post_lab_11' : '10', 'pre_lab_12' : '10', 'in_lab_12' : '10', 'post_lab_12' : '10'}
	)
	context = {
		"form": form
	}

	if form.is_valid():
		CS2150.objects.all().delete()
		obj = form.save(commit=False)
		obj.save()
		form.save_m2m()

		return redirect('cs2150_result')

	return render(request, template, context)

def cs2150_result(request):
	template = "cs2150_result.html"
	gradebook = CS2150.objects.all()[0]
	final_percentage = float(gradebook.final_actual) / float(gradebook.final_max)
	exam_1_percentage = float(gradebook.exam_1_actual) / float(gradebook.exam_1_max)
	exam_2_percentage = float(gradebook.exam_2_actual) / float(gradebook.exam_2_max)

	lab_actual = float(gradebook.pre_lab_1) + float(gradebook.in_lab_1) + float(gradebook.post_lab_1) \
	+ float(gradebook.pre_lab_2) + float(gradebook.in_lab_2) + float(gradebook.post_lab_2) \
	+ float(gradebook.pre_lab_3) + float(gradebook.in_lab_3) + float(gradebook.post_lab_3) \
	+ float(gradebook.pre_lab_4) + float(gradebook.in_lab_4) + float(gradebook.post_lab_4) \
	+ float(gradebook.pre_lab_5) + float(gradebook.in_lab_5) + float(gradebook.post_lab_5) \
	+ float(gradebook.pre_lab_6) + float(gradebook.in_lab_6) + float(gradebook.post_lab_6) \
	+ float(gradebook.pre_lab_7) + float(gradebook.in_lab_7) + float(gradebook.post_lab_7) \
	+ float(gradebook.pre_lab_8) + float(gradebook.in_lab_8) + float(gradebook.post_lab_8) \
	+ float(gradebook.pre_lab_9) + float(gradebook.in_lab_9) + float(gradebook.post_lab_9) \
	+ float(gradebook.pre_lab_10) + float(gradebook.in_lab_10) + float(gradebook.post_lab_10) \
	+ float(gradebook.pre_lab_11) + float(gradebook.in_lab_11) + float(gradebook.post_lab_11) \
	+ float(gradebook.pre_lab_12) + float(gradebook.in_lab_12)
	lab_max = float(gradebook.lab_1_max) + float(gradebook.lab_2_max) + float(gradebook.lab_3_max) + float(gradebook.lab_4_max) \
	+ float(gradebook.lab_5_max) + float(gradebook.lab_6_max) + float(gradebook.lab_7_max) + float(gradebook.lab_8_max) \
	+ float(gradebook.lab_9_max) + float(gradebook.lab_10_max) + float(gradebook.lab_11_max) + float(gradebook.lab_12_max)
	lab_percentage = lab_actual / lab_max
	
	final_weighted = final_percentage * 25
	exam_1_weighted = exam_1_percentage * 15
	exam_2_weighted = exam_2_percentage * 15
	lab_weighted = lab_percentage * 45
	
	gradebook.grade = round(lab_weighted + exam_1_weighted + exam_2_weighted + final_weighted, 2)

	if gradebook.grade >= 97:
		gradebook.letterGrade = 'A+'
	elif 93 <= gradebook.grade < 97:
		gradebook.letterGrade = 'A'
	elif 90 <= gradebook.grade < 93:
		gradebook.letterGrade = 'A-'
	elif 87 <= gradebook.grade < 90:
		gradebook.letterGrade = 'B+'
	elif 83 <= gradebook.grade < 87:
		gradebook.letterGrade = 'B'
	elif 80 <= gradebook.grade < 83:
		gradebook.letterGrade = 'B-'
	elif 77 <= gradebook.grade < 80:
		gradebook.letterGrade = 'C+'
	elif 73 <= gradebook.grade < 77:
		gradebook.letterGrade = 'C'
	elif 70 <= gradebook.grade < 73:
		gradebook.letterGrade = 'C-'
	elif 67 <= gradebook.grade < 70:
		gradebook.letterGrade = 'D+'
	elif 63 <= gradebook.grade < 67:
		gradebook.letterGrade = 'D'
	elif 60 <= gradebook.grade < 63:
		gradebook.letterGrade = 'D-'
	else:
		gradebook.letterGrade = 'F'

	context = {
		'gradebook': gradebook,
		'final_percentage': round(final_percentage * 100, 2),
		'exam_1_percentage': round(exam_1_percentage * 100, 2),
		'exam_2_percentage': round(exam_2_percentage * 100, 2),
		'lab_actual': lab_actual,
		'lab_max': lab_max,
		'lab_percentage': round(lab_percentage * 100, 2),
		'final_weighted': round(final_weighted, 2),
		'exam_1_weighted': round(exam_1_weighted, 2),
		'exam_2_weighted': round(exam_2_weighted, 2),
		'lab_weighted': round(lab_weighted, 2)
	}

	return render(request, template, context)
