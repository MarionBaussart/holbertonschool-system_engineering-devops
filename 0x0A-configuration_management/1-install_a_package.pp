# install puppet-lint
exec { 'puppet-lint':
    command  => 'gem install puppet-lint 2.5.0',
    path     => '/usr/bin',
}
