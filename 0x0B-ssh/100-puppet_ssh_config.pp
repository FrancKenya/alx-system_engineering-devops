# This file uses Puppet to make changes to a configuration file

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => "
        Host 315017-web-01
        HostName 54.227.197.97
        User ubuntu
        IdentityFile ~/.ssh/school
    ",
    mode    => '0600',
}
