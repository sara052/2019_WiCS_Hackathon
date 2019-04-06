from django import forms
from gradebook.models import *

class cs2150Gradebook(forms.ModelForm):
	class Meta:
		model = CS2150
		fields = [
			# 'grade', 
			'final_actual', 'final_max', 'exam_1_actual', 'exam_1_max', 'exam_2_actual', 'exam_2_max',
			'pre_lab_1', 'in_lab_1', 'post_lab_1', 'lab_1_max', 'pre_lab_2', 'in_lab_2', 'post_lab_2', 'lab_2_max',
			'pre_lab_3', 'in_lab_3', 'post_lab_3', 'lab_3_max', 'pre_lab_4', 'in_lab_4', 'post_lab_4', 'lab_4_max',
			'pre_lab_5', 'in_lab_5', 'post_lab_5', 'lab_5_max', 'pre_lab_6', 'in_lab_6', 'post_lab_6', 'lab_6_max',
			'pre_lab_7', 'in_lab_7', 'post_lab_7', 'lab_7_max', 'pre_lab_8', 'in_lab_8', 'post_lab_8', 'lab_8_max',
			'pre_lab_9', 'in_lab_9', 'post_lab_9', 'lab_9_max', 'pre_lab_10', 'in_lab_10', 'post_lab_10', 'lab_10_max',
			'pre_lab_11', 'in_lab_11', 'post_lab_11', 'lab_11_max', 'pre_lab_12', 'in_lab_12', 'lab_12_max',
		]

	def __init__ (self, *args, **kwargs):
		super(cs2150Gradebook, self).__init__(*args, **kwargs)

		# self.fields["grade"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["final_actual"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["final_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["exam_1_actual"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["exam_1_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["exam_2_actual"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["exam_2_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_1"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_1"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_1"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_1_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_2"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_2"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_2"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_2_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_3"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_3"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_3"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_3_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_4"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_4"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_4"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_4_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_5"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_5"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_5"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_5_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_6"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_6"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_6"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_6_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_7"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_7"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_7"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_7_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_8"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_8"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_8"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_8_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_9"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_9"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_9"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_9_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_10"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_10"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_10"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_10_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_11"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_11"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["post_lab_11"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_11_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["pre_lab_12"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["in_lab_12"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
		self.fields["lab_12_max"].widget = forms.widgets.Textarea(attrs={'cols': 10, 'rows': 1})
