# creating a custom HTTP header response
exec { 'update':
    command => 'apt update -y',
}

package { 'nginx':
    ensure  => installed,
    require => Package['update'],
}

file_line { 'header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
