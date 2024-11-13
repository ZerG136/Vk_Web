from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse
from askme.question import Card, Question, Answer

username = 'User'
user_avatar = 'img/person-circle.svg'

tags = [(f'tag{i}', 'tag') for i in range(1, 11)]
members = ["Member1", "Member2", "Member3", "Member4", "Member5"]

cards = [
    Card('img/person-circle.svg',
         f'How to do {i + 1}?',
         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna...',
         ['tag_1', 'tag_2'], i, i
    )
    for i in range(10)
]
main_question = Question('img/person-circle.svg',
                         f'How to do ...?',
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna...',
                         ['tag_1', 'tag_2'],
                         9)
answers = [
    Answer('img/person-circle.svg',
           f'How to do {i + 1}.',
           'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna...',
           ['tag_1', 'tag_2'],
           1,
           False
    )
    for i in range(10)
]

def paginate(obj_list, req, per_page=3):
    paginator = Paginator(obj_list, per_page)
    page_number = req.GET.get('page', 1)

    try:
        return paginator.get_page(page_number)
    except PageNotAnInteger:
        return paginator.get_page(1)
    except EmptyPage:
        return paginator.get_page(paginator.num_pages)

def ask(req):
    return TemplateResponse(req, 'ask.html', context={'members': members,
                                                      'tags': tags,
                                                      'user_avatar': user_avatar,
                                                      'username': username})

def hot(req):
    paginated_cards = paginate(cards, req, 4)

    return TemplateResponse(req, 'hot.html', context={'members': members,
                                                      'tags': tags,
                                                      'user_avatar': user_avatar,
                                                      'username': username,
                                                      'cards': paginated_cards})

def index(req):
    paginated_cards = paginate(cards, req, 4)

    return TemplateResponse(req, 'index.html', context={'username': username,
                                                        'user_avatar': user_avatar,
                                                        'members': members,
                                                        'tags': tags,
                                                        'cards': paginated_cards})


def login(req):
    return TemplateResponse(req, 'login.html', context={'members': members, 'tags': tags})

def question(req):
    paginated_answers = paginate(answers, req, 3)

    return TemplateResponse(req, 'question.html', context={'members': members,
                                                           'tags': tags,
                                                           'user_avatar': user_avatar,
                                                           'username': username,
                                                           'cards': paginated_answers,
                                                           'question': main_question})

def settings(req):
    return TemplateResponse(req, 'settings.html', context={'members': members,
                                                           'tags': tags,
                                                           'user_avatar': user_avatar,
                                                           'username': username})

def signup(req):
    return TemplateResponse(req, 'signup.html', context={'members': members, 'tags': tags})

def tag(req):
    paginated_cards = paginate(cards, req, 4)

    return TemplateResponse(req, 'tag.html', context={'members': members,
                                                      'tags': tags,
                                                      'user_avatar': user_avatar,
                                                      'username': username,
                                                      'cards': paginated_cards})
