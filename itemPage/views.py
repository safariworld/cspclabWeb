# Create your views here.
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from itemPage.models import itemList, borrowedList
from django.template import Context, loader

import md5

#template: itemPage/itemList.html

def itemListView( request, page=1 ):
#    all_item_list = itemList.objects.all()
#    return render_to_response( 'itemPage/itemList.html', {'all_item_list': all_item_list} )
#    return HttpResponse()
    page = int(page)
    per_page = 15 
    start_pos = (page-1)*per_page
    end_pos = start_pos+per_page

    item_entries = itemList.objects.raw( '''SELECT a.id, a.category, 
                                                   a.itemName, 
                                                   a.available, 
                                                   b.borrowedDate 
                                            FROM itemPage_itemlist AS a 
                                            LEFT OUTER JOIN itemPage_borrowedlist AS b 
                                            ON a.id=b.itemCode_id 
                                            AND returnDate is null
                                            ORDER BY a.id''')[start_pos:end_pos]
    item_count = itemList.objects.count()
    page_count = ( item_count/per_page ) + (( item_count % per_page )!=0)
    tpl = loader.get_template( 'itemPage/itemList.html' )
    page_count_start = page_count/10+1
    if page/10 == page_count/10:
        page_count_end = page_count+1
    else:
        page_count_end = page_count/10+11

    ctx = Context({ 
        'item_entries':item_entries,
        'current_page':page,
        'prev_page':page-1,
        'next_page':page+1,
        'end_page':page_count,
        'page_count':range(page_count_start,page_count_end)
        })
    #    return render_to_response( 'itemPage/itemList.html', {'item_entries': item_entries} )
    return HttpResponse(tpl.render(ctx))

