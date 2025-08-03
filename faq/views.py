from django.shortcuts import render, redirect
from django.urls import reverse
from .models import FAQ
import difflib

def find_best_match(user_question, lang):
    questions = FAQ.objects.filter(language=lang).values_list('question', flat=True)
    lower_qs = [q.lower() for q in questions]
    matches = difflib.get_close_matches(user_question.lower(), lower_qs, n=1, cutoff=0.4)
    if matches:
        matched = next((q for q in questions if q.lower() == matches[0]), None)
        answer = FAQ.objects.filter(language=lang, question=matched).first()
        return answer.answer if answer else None
    return None

def chatbot(request):
    selected_lang = request.GET.get('lang', 'pl')
    response = ''

    if request.method == 'POST':
        selected_lang = request.POST.get('language', 'pl')
        user_question = request.POST.get('question', '').strip()

        answer = find_best_match(user_question, selected_lang)
        if answer:
            request.session['chat_response'] = answer
        else:
            request.session['chat_response'] = (
                "Nie znam odpowiedzi na to pytanie. Spróbuj inaczej!"
                if selected_lang == 'pl'
                else "I don't know the answer to that. Try again!"
            )

        return redirect(f"{reverse('chatbot')}?lang={selected_lang}")

    response = request.session.pop('chat_response', '')

    return render(request, 'faq/chat.html', {
        'response': response,
        'selected_lang': selected_lang,
        'is_english': selected_lang == 'en',
    })
