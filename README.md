Contributors
===

* Kokan <kokaipeter@gmail.com>
* Griggs <beke.zoltan00@gmail.com>
* amatyi96 <amatyi96@inf.elte.hu>
* Borbs <ron.borbenyi@gmail.com>
* Hrvthp <hrvth0@gmail.com>
* BF (not member of the coding subgroup)
* gergely22mucsi <gergely22mucsi@gmail.com>
* tarczi <tarczalitamas97@gmail.com>

***

Running the application
===
Setting up database
---
You can set up the initial database with running the following command:
>python manage.py migrate

Starting the application
---
To start the application, simply run the following code snippet in command prompt:
>python manage.py runserver

***

Translation
===
How to set up translation:
1. In 'settings.py' insert the following code snippet:

>\# Languages<br>
>\# https://docs.djangoproject.com/en/2.2/ref/settings/#languages<br>
>
>\# Expand this list with any other language you want...<br>
><b>LANGUAGES = [<br>
>    ('hu', _('Hungarian')),<br>
>    ('en', _('English')),<br>
>]</b><br>
>
>\# If you set this to False, Django will make some optimizations so as not to load the internationalization machinery.<br>
>\# Make sure it is set to 'True' if you want to support localization<br>
><b>USE_I18N = True</b><br>
>
>\# If you set this to False, Django will not format dates, numbers and calendars according to the current locale.<br>
><b>USE_L10N = True</b><br>
>
>\# Set the default language for your site.<br>
><b>LANGUAGE_CODE = 'en'</b><br>
>

>\# Contains the path list where Django should look into for django.po files for all supported languages<br>
><b>LOCALE_PATHS = [<br>
>    os.path.join(BASE_DIR, 'locale'),<br>
>]</b><br>

2. Load 'i18n' in every file you want to translate and flag the static texts with 'trans' tag like this:

>\{% load i18n %}<br>
>\<h1><b>{% trans 'Sign Up' %}</b>\</h1><br>
>\<form><br>
>    \<label><b>{% trans 'Username' %}</b>\</label><br>
>    \<input id='username' type='text'/><br>
>    \<label><b>{% trans 'Password' %}</b>\</label><br>
>    \<input id='password' type='password'/><br>
>\</form><br>

3. Generate translation files. In the folder with contains the 'manage.py' file run the following command with the desired language:
>$ python manage.py makemessages -l 'hu'<br>
>$ python manage.py makemessages -l 'en'<br>

4. In the '/locale/<language>/LC_MESSAGES/django.po' file translate the texts. For example:
>#: .\simple_managing_names\templates\names\index.html:15<br>
>msgid "Delete"<br>
>msgstr "Törlés"<br>
  
5. Then compile the static translation messages with the following command:
>$ python manage.py compilemessages

6. Run server and change 'LANGUAGE_CODE' in 'settings.py'.
