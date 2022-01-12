def response(status=None, size=None, message=None, data=None, rc=None):
    response = {}
    response.update({ 's': status })

    if size is not None:
        response.update({ 'size': size })

    if message is not None:
        response.update({ 'm': message })

    if data is not None:
        response.update({ 'd': data })

    if rc is not None:
        response.update({ 'rc': rc })

    return response