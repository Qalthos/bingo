from pyramid.view import view_config

from bingo.widgets import BingoBoard


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return dict(board=BingoBoard('board').board)
