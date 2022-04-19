# install puppet-lint
package { 'puppet-lint':
    command => 'sudo gem install puppet-lint',
    path    => '/usr/bin',
}
