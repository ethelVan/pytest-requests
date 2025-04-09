class CaseData:

    def __init__(self, *args, **kwargs):
        for i in list(*args):
            setattr(self, i[0], i[1])
