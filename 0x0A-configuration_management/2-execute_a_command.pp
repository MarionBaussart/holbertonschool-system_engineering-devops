# create a manifest that kills a process named killmenow
exec { 'kills a process named killmenow':
    command  => 'pkill killmenow',
    path     => '/bin/bash',
}
