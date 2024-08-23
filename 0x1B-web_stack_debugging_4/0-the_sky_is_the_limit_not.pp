# A Puppet manifest to fix a server request failure under high load by updating Nginx settings

file_line { 'increase nginx worker connections':
  path   => '/etc/default/nginx',
  line   => 'worker_connections 4096;',
  match  => '^worker_connections\s+\d+;',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
