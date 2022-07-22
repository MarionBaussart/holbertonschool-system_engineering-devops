# install puppet-lint
exec { 'flask':
    command => 'sudo gem install flask -v2.1.0',
    path    => ['/usr/bin'],
}
