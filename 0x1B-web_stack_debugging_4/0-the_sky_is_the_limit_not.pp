# A Puppet manifest to fix a server request failure under high load by updating Nginx settings

exec {'write':
  provider => shell,
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx'
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart'
}
