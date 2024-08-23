# A Puppet manifest to update the OS configuration so that the holberton user can open files without errors

file_line { 'increase nofile limit to 50000':
  path  => '/etc/security/limits.conf',
  line  => '*               -       nofile          50000',
  match => '^\*\s+-\s+nofile\s+\d+',
}

file_line { 'increase nofile limit to 40000':
  path  => '/etc/security/limits.conf',
  line  => '*               soft    nofile          40000',
  match => '^\*\s+soft\s+nofile\s+\d+',
}
