from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Assignment

def assignment_list(request):
    assignments = Assignment.objects.all().order_by('-uploaded_at')
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

def download_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    response = FileResponse(assignment.file, as_attachment=True)
    return response