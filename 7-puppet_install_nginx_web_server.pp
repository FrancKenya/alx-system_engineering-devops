# A manifest that's used to configure a nginx server
package {' nginx':
        ensure   => installed;
}
exec {'update apt-get and install':
    command  => 'sudo apt-get update && sudo apt-get install nginx'
    path     =>  '/usr/bin:/usr/sbin:/bin',
    provider =>  shell
}
# Set up Nginx service
service { 'nginx':
    ensure => running,
    enable => true,
}
# Create a custom index.html page for the root URL
file { '/var/www/html/index.html':
    ensure  => present,
    content => "Hello World!\n",
    require => Package['nginx'],
}
# handle redirection

exec {'redirection':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me \/ permanent;/" /etc/nginx/sites-available/default',
  provider => shell,
}
# Allow nginx through firewall

exec { 'allow firewall':
    command => 'ufw allow "NGINX Full"',
    path    => '/usr/bin:/usr/sbin:/bin',
  provider  => shell,
}
exec { 'restart nginx':
    command => 'sudo service nginx restart',
    path    => '/usr/bin:/usr/sbin:/bin',
  provider  => shell,
}
