This is a quick django app to collect comments for a crowdsourced letter of recommendation.  I wrote it as I was applying to a 
PhD program to work on solar energy and realized that I only know two other people in the world, and it doesn't look all that 
impressive when your mom writes your rec letter.

Django-wise, this is a pretty simple program.  There are two apps:  letter and recommendation.  Letter handles all the templating and views for the project, and recommendation just contains a class that holds the info from a recommendation.  It's running off a sqlite db for maximum portability.  




Thanks to [Subtle Patterns](http://subtlepatterns.com/) for the background images, and to [W3Schools](http://www.w3schools.com/) and [Stack Overflow](http://stackoverflow.com/) for answering my endless questions about django and CSS

I spent like three hours figuring out a good system that I could use to serve static files with apache for future django experiments, and I ended up making two folders in my
home directory, media and static.  Whenever I create a new django project, I put a folder into media and static with that name, symlink it into my django project directory so everything is in one place, and then I set up an apache alias to serve those static directories.  I like this a lot better than the nasty, ad-hoc way I did it before, which was to slap a symlinked folder into some other website's content directory and treat that rando directory as my static folder.  
I know, I know.

~
 |-media
 | |-recLetter
 | |-solarPocketFactory
 | |-other django projects
 |-static
   |-recLetter
   |-solarPocketFactory
   |-other django projects

And just to throw in the kitchen sink, here's my virtual host configuration from apache.

       <VirtualHost *:80>   #recletter
             ServerName recLetter.artiswrong.com
	     ServerAlias recletter.*

             <IfModule mod_rewrite.c>
                 RewriteEngine On
	     </IfModule>

             Alias /robots.txt /home/japhy/recLetter/static/robots.txt
             Alias /favicon.ico /home/japhy/recLetter/static/favicon.ico

             AliasMatch ^/([^/]*\.css) /home/japhy/static/recLetter/css/$1

             Alias /media/ /home/japhy/media/recLetter/
             Alias /static/ /home/japhy/static/recLetter/
             WSGIScriptAlias / /home/japhy/recLetter/Apache/django.wsgi
              <Directory /home/japhy/recLetter/Apache/>
                  Order deny,allow
                  Allow from all
              </Directory>


            ErrorLog /var/log/apache2/recLetter-error.log
            # Possible values include: debug, info, notice, warn, error, crit,
            # alert, emerg.
            LogLevel warn

            CustomLog /var/log/apache2/recLetter-access.log combined
	</VirtualHost>
