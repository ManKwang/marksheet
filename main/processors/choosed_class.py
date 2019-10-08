def is_choosed(request):
    choosed = False

    if request.GET.get('c_id'):
        choosed = True

    return {'CLASS_CHOOSED': choosed, 'CLASS_ID': request.GET.get('c_id')}
