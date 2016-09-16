from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import FileForm
import os, csv

from . import dedupe_lib
from django.utils.encoding import smart_str


def index(request):
  return render(request,"main/home.djt",{})


def selcol(request):
	global saved_file
	saved = False
	if request.method == "POST":
		myFile = FileForm(request.POST, request.FILES)
		if myFile.is_valid():
			saved_file = UploadFile()
			saved_file.file_name = myFile.cleaned_data["file_name"]
			saved_file.file = myFile.cleaned_data["file"]
			saved_file.save()
			saved = True
	else:
		myFile = UploadFileForm()
		return render(request,"main/home.djt",{'form' : myFile})

	return render(request,"main/selcol.djt",{'file_name': saved_file.file_name,'file_path':'media/'+str(saved_file.file), 'cols':col_names()})


def col_names():
	with open(str(os.getcwd())+"/media/"+str(saved_file.file)) as f:
		reader = csv.reader(f)
		for row in reader:
			return row


def get_answer(request):
	for i in request.POST:
		label = request.POST[i]
		break
	if label == "f":
		dedupe_lib.active_train()
		dedupe_lib.rundedupe2()
		return render(request, "main/finish.djt")
	else:
		dedupe_lib.mark(label)
		return ask_question(request)

def ask_question(request):
	que = dedupe_lib.generate_question();
	return render(request, "main/ask_que.djt", {'que': que})

def active_learning(request):
	l = []
	for col_name in request.POST:
		if not col_name in ["csrfmiddlewaretoken", "file_path"]:
			l.append(str(col_name))
	is_active_labelling = dedupe_lib.rundedupe(os.getcwd()+"/media/"+str(saved_file.file), "Id", l)
	if is_active_labelling :
		return ask_question(request)
	dedupe_lib.rundedupe2()
	return render(request, "main/finish.djt")
	# return HttpResponse(request.POST)

def download(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str("dedupe-output.csv")
	# response['X-Sendfile'] = smart_str("/media/output_files/output.csv")

	with open(os.getcwd()+"/media/output_files/output.csv") as f_input:
		reader = csv.reader(f_input)
		writer = csv.writer(response)

		for row in reader:
			writer.writerow(row)
	return response
		

