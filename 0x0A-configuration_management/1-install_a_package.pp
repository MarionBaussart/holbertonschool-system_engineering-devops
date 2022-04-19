# install puppet-lint
exec { 'puppet-lint':
    command => 'sudo gem install puppet-lint',
    path    => '/usr/bin',
}
