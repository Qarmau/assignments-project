from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Assignment

def class_list(request):
    class_list = Assignment.objects.all().order_by('grade')
    
    # Extract unique years
    unique_class_list = []
    unique_grade= set()
    for clist in class_list:
        if clist.grade not in unique_grade:
            unique_class_list.append(clist)
            unique_grade.add(clist.grade)
    return render(request,'assignments/class_list.html',{'class_list':unique_class_list})

def assignment_list(request, assignment_list_id):
    # Retrieve the specific holiday assignment using holiday_id
    assignment_list = get_object_or_404(Assignment, id=assignment_list_id)

    # Retrieve all assignments for the selected year and order them by date uploaded
    all_assignments = Assignment.objects.filter(grade=assignment_list.grade).order_by('-subject')

   

    #return render(request, 'holiday.html', {'holiday': holiday, 'assignment_list': filtered_assignments})
    
    return render(request, 'assignments/assignment_list.html', {'assignment_list': assignment_list,'assignment_list': all_assignments})


def download_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    response = FileResponse(assignment.file, as_attachment=True)
    return response 
