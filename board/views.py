# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from board.models import WritingEntries, Categories, CommentsModel
from django.template import Context, loader
import md5
from forms import WriteForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
import settings
import os
from django.core.servers.basehttp import FileWrapper
from django.contrib.auth.decorators import login_required

from django.template import RequestContext
from django.shortcuts import render_to_response

#show list page specified by arguement PAGE.
#template: list.html

def list ( request, board_category, page=1 ):
    
    page_title = 'List'
    per_page = 5
    page = int(page)
    start_pos = (page-1)*per_page
    end_pos = start_pos + per_page
    category = get_object_or_404(Categories, title = board_category)
    entries = WritingEntries.objects.filter(category=category).order_by('-createdDate')[start_pos:end_pos]
    numberOfentries = WritingEntries.objects.count()
    numberOfpages = numberOfentries/per_page
    if not numberOfentries%per_page == 0:
        numberOfpages = numberOfpages + 1

    var = RequestContext(request, {
        'page_title':page_title,
        'entries':entries,
        'current_page':page,
        'num_pages':[ t+1 for t in range(numberOfpages)],
        'category':board_category,
        })
    return render_to_response(
            'list.html',
            var,
            )

def read ( request, entry_id = None ):
    page_title = 'Read page'
    current_entry = get_object_or_404(WritingEntries, id = entry_id)
    cmts = CommentsModel.objects.filter(writingEntry=current_entry).order_by('createdDate')
    tpl = loader.get_template('read.html')
    form = CommentForm()
    ctx = Context({
        'page_title':page_title,
        'current_entry':current_entry,
        'comments':cmts,
        'form':form
        })
    
    return HttpResponse(tpl.render(ctx))

def handle_uploaded_file(f):
    destination = open('attachments/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write( chunk )
    destination.close()

@csrf_exempt
@login_required
def write( request, board_category ):
    initial_data = {}
    category = get_object_or_404(Categories, title = board_category)
    initial_data["category"] = category.id
    tpl = loader.get_template('write.html')
    if request.method == "POST":
        form = WriteForm(request.POST, request.FILES)
        if form.is_valid():
            if len(request.FILES) != 0:
                handle_uploaded_file(request.FILES['attachedFile'])
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            tpl = loader.get_template('main.html')
            ctx = Context({})
            return HttpResponse( tpl.render(ctx) )
        else:
            ctx = Context({
                'form':form
            })
            return HttpResponse( tpl.render(ctx) )
    else:
        form = WriteForm(initial=initial_data)
        ctx = Context({
            'form':form
            })
        return HttpResponse( tpl.render(ctx) )

def download_file(request, filename ):
    filepath = settings.DOWNLOAD_DIR + filename
    wrapper = FileWrapper( file(filepath) )
    response = HttpResponse( wrapper, mimetype='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=' + filename.encode('utf-8')
    response['Content-Length'] = os.path.getsize(filepath)

    return response

#add comments according to some writing.
#name, password, content, entry_id
def add_comment(request):

    cmt_name = request.POST.get('name', '')
    if not cmt_name.strip():
        return HttpResponse('Please write name')

    cmt_password = request.POST.get('password', '')
    if not cmt_password.strip():
        return HttpResponse('Please write password')
    cmt_password = md5.md5(cmt_password).hexdigest()

    cmt_content = request.POST.get('content', '')
    if not cmt_content.strip():
        return HttpResponse('Write content')

    
    if request.POST.has_key('entry_id') == False:
        return HttpResponse('Select write')
    else:
        try:
            entry=WritingEntries.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('There is no such write')

    try:
        new_cmt = CommentsModel(name=cmt_name, password=cmt_password, content=cmt_content, writingEntry=entry)
        new_cmt.save()
        entry.comments += 1
        entry.save()
        return HttpResponse('Successfully registerd')
    except:
        return HttpResponse('There is error')

    return HttpResponse('Error!!')

def delete_comment(request):
    cmt_password = request.POST.get('password', '')
    cmt_password = md5.md5(cmt_password).hexdigest()

    del_entry = request.POST.get('cmt', '')
    return HttpResponse('%s'%del_entry.id)
    try:
        if del_entry.password == cmt_password:
            del_entry.delete()
            return HttpResponse('Deleted!.!')
        else:
            return HttpResponse('Wrong password')
    except:
        return HttpResponse('Error!!')

