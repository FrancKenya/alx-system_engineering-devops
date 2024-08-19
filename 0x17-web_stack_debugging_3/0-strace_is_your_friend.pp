# Rectifying the Internal Server Error to deliver a webpage when queried

exec { 'replace_phpp_with_php':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep "phpp" /var/www/html/wp-settings.php',
  }
