# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from board.models import WritingEntries, Categories, CommentsModel
from django.template import Context, loader
import md5

#show list page specified by arguement PAGE.
#template: list.html

def indexView ( request, page=1 ):

    page_title = 'List'
    per_page = 5

    page = int(page)

    start_pos = (page-1)*per_page
    end_pos = start_pos + per_page

    entries = WritingEntries.objects.all().order_by('-createdDate')[start_pos:end_pos]
    numberOfentries = WritingEntries.objects.count()
    numberOfpages = numberOfentries/per_page
    if not numberOfentries%per_page == 0:
        numberOfpages = numberOfpages + 1

    tpl = loader.get_template('list.html')
    ctx = Context({
        'page_title':page_title,
        'entries':entries,
        'current_page':page,
        'num_pages':[ t+1 for t in range(numberOfpages)],
        })
    
    return HttpResponse(tpl.render(ctx) )

def read ( request, entry_id = None ):

    page_title = 'Read page'
    try:
        current_entry = WritingEntries.objects.get(id = int(entry_id))
    except:
        return HttpResponse('There is no such write.')
    try:
        prev_entry = current_entry.get_previous_by_updatedDate()
    except:
        prev_entry = None

    try:
        next_entry = current_entry.get_next_by_updatedDate()
    except:
        next_entry = None

    cmts = CommentsModel.objects.filter(writingEntry=current_entry).order_by('updatedDate')
    tpl = loader.get_template('read.html')
    ctx = Context({
        'page_title':page_title,
        'current_entry':current_entry,
        'prev_entry':prev_entry,
        'next_entry':next_entry,
        'comments':cmts
        })
    
    return HttpResponse(tpl.render(ctx))

def write_form( request ):
    page_title = 'Write page'

    categories = Categories.objects.all()

    tpl = loader.get_template('write.html')
    ctx = Context({
        'page_title':page_title,
        'categories':categories
        })

    return HttpResponse( tpl.render(ctx) )

def add_post( request ):
    if request.POST.has_key('title') == False:  
        return HttpResponse('Please write content')
    else:
        if len(request.POST['title']) == 0:
            return HttpResponse("The length of title is at least 1.")
        else:
            if request.POST.has_key('content') == False:
                return HttpResponse('Write content.')
            else:
                entry_content = request.POST['content']
                try:
                    entry_category = Categories.objects.get(id = request.POST['category'])
                except:
                    return HttpResponse('Weird Category')

                entry_title = request.POST['title']
                new_entry = WritingEntries( title = entry_title, content = entry_content, category = entry_category)

                # save
                try:
                    new_entry.save()
                except:
                    return HttpResponse('Error at 1 storing')
                
                return HttpResponse('%s write has been stored successfully.' % new_entry.id)


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
    
    
    
