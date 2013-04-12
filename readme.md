
	<VirtualHost *:80>   #recletter
	        ServerName recletter.artiswrong.com
     		ServerAlias recletter.*

		 <IfModule mod_rewrite.c>
		 RewriteEngine On
		 </IfModule>	

                Alias /robots.txt /home/japhy/recLetter/static/robots.txt
                Alias /favicon.ico /home/japhy/recLetter/static/favicon.ico

                AliasMatch ^/([^/]*\.css) /home/japhy/recLetter/static/css/$1

                Alias /media/ /home/japhy/recLetter/media/
                Alias /static/ /home/japhy/recLetter/static/

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