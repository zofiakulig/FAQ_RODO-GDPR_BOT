# FAQ RODO‑GDPR Chatbot
This is a Django application that answers frequently asked questions about the EU's GDPR regulation.
Users can ask in Polish or English, and the bot searches its FAQ database for the closest match, returning the corresponding answer.

## Live
**Chatbot:** https://faq-rodo-gdpr-bot.onrender.com/
<br>
**Admin panel:** https://faq-rodo-gdpr-bot.onrender.com/admin (You can use these credentials to view the admin panel without edit privileges. - Username: test_user, Password: 123test123)

## Key Features
* FAQ model storing question/answer pairs with language code (pl or en).
* Approximate matching via difflib to find relevant answers even with varied wording.
* Web interface for language selection, question submission, and answer display.
* Admin site for managing FAQ entries.
* Environment-based configuration with .env support.
* Deployable using Gunicorn and Whitenoise.
