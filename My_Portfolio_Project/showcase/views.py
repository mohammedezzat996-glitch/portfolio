from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project, Category, Skill, ContactMessage

def home(request):
    # جلب آخر 3 مشاريع مضافة مباشرة لواجهة المستخدم العادي
    featured_projects = Project.objects.all()[:3]
    skills = Skill.objects.all()
    categories = Category.objects.all()
    
    # جلب جميع الرسائل العامة لعرضها كصندوق محادثة (من الأقدم للأحدث)
    user_messages = ContactMessage.objects.all().order_by('id')
    
    # معرفة الرسائل التي تخص هذا المتصفح الحالي فقط لحمايتها من الحذف والتعديل
    my_message_ids = request.session.get('user_message_ids', [])
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        message_id = request.POST.get('message_id')
        
        if message_id: # التعديل (يتم فقط لو كانت الرسالة ملك للمستخدم)
            if int(message_id) in my_message_ids:
                msg_obj = get_object_or_404(ContactMessage, id=message_id)
                msg_obj.name = name
                msg_obj.email = email
                msg_obj.subject = subject
                msg_obj.message = message
                msg_obj.save()
                messages.success(request, 'تم تعديل رسالتك بنجاح!')
            else:
                messages.error(request, 'غير مسموح لك بتعديل هذه الرسالة!')
        else: # إضافة رسالة جديدة
            if name and email and message:
                new_msg = ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
                my_message_ids.append(new_msg.id)
                request.session['user_message_ids'] = my_message_ids
                messages.success(request, 'تم إرسال مشاركتك!')
                
        return redirect('home')
            
    return render(request, 'showcase/home.html', {
        'featured_projects': featured_projects, 
        'skills': skills, 
        'categories': categories,
        'user_messages': user_messages,
        'my_message_ids': my_message_ids
    })

def projects_gallery(request):
    # جلب كافة المشاريع لصفحة المعرض الكامل مباشرة للزوار دون شروط معقدة
    projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, 'showcase/gallery.html', {'projects': projects, 'categories': categories})

def project_detail(request, pk):
    # جلب تفاصيل مشروع معين
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'showcase/detail.html', {'project': project})

def delete_message(request, pk):
    # لا يمكن الحذف إلا إذا كان المستخدم هو صاحب الرسالة فعلياً
    my_message_ids = request.session.get('user_message_ids', [])
    if pk in my_message_ids:
        msg_obj = get_object_or_404(ContactMessage, id=pk)
        msg_obj.delete()
        my_message_ids.remove(pk)
        request.session['user_message_ids'] = my_message_ids
        messages.success(request, 'تم حذف الرسالة بنجاح!')
    else:
        messages.error(request, 'لا تملك صلاحية حذف هذه الرسالة!')
    return redirect('home')