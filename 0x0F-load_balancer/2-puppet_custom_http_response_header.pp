# creates a custom HTTP header response
exec {'update':
    command  => 'sudo apt-get -y update',
}
package {'Nginx':
    ensure => installed
}

exec {'add_header':
    command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\
tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
    environment => ['HOST={hostname}'],
}

-> exec {'restart Nginx':
    command  => 'sudo service nginx restart',
}
