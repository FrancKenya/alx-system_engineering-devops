# installing nginx

package { 'nginx':
        ensure          => installed,
        provider        => 'apt',
        install_options => ['-y'],
}

exec { 'delete html files':
        command => 'sudo rm -rf /var/www/html/*.html',
        path    => ['/usr/bin', '/usr/sbin', '/usr/bin/env'],
}

# starting nginx
exec { 'start nginx':
        command => 'sudo service nginx start',
        path    => ['/usr/bin', '/usr/sbin', '/usr/bin/env'],
}

file { '/var/www/html/index.html':
        ensure  => present,
        content =>
'Hello World!
',
}

# adding error 404 file
file { '/var/www/html/error404.html':
    ensure  => present,
    content =>
'Ceci n\'est pas une page
',
}

# editing sites-enabled file
file { '/etc/nginx/sites-enabled/default':
        ensure  => present,
        path    => '/etc/nginx/sites-enabled/default',
        content =>
'server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        # 404 error file
        error_page 404 /error404.html;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
}
',
}

# editing sites-available

file { '/etc/nginx/sites-available/default':
        ensure  => present,
        path    => '/etc/nginx/sites-available/default',
        content =>
'server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;
    
        server_name _;

        # 404 error file
        error_page 404 /error404.html;
    
        location / {
                try_files $uri $uri/ =404;
        }

        # redirecting user
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
}
',
}

#restarting nginx
exec { 'restart nginx':
    command => 'sudo service nginx restart',
    path    => ['/usr/bin', '/usr/sbin', '/usr/bin/env'],
}
